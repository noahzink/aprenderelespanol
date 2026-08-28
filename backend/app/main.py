"""from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel

import unicodedata

from app.database import (
    init_db, create_user, authenticate_user,
    get_user_by_token, add_user_xp, save_exercise_score, get_user_scores
)
from app.data import CURRICULUM_DB, QUESTIONS_DB
from app.models import (
    UserRegister, UserLogin, AuthResponse, UserProfile,
    QuestionResponse, AnswerSubmission, ValidationResult
)

app = FastAPI(title="Aprende Español API", version="1.0.0")
"""

from fastapi import FastAPI, HTTPException, Header, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Dict, Any
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from starlette.responses import FileResponse
from app.models import UserRegister, UserLogin, AuthResponse, UserProfile, ValidationResult, AnswerSubmission
from app.database import (
    init_db, create_user, authenticate_user,
    get_user_by_token, add_user_xp, save_exercise_score, get_user_scores
)
from app.data import CURRICULUM_DB, QUESTIONS_DB
import unicodedata, os
app = FastAPI(title="Aprende Español API")

"""
# Chemin vers le dossier frontend (remonte d'un niveau si Root Directory = backend)
frontend_path = os.path.join(os.path.dirname(__file__), "..", "..", "frontend")

if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

    @app.get("/")
    def serve_home():
        return FileResponse(os.path.join(frontend_path, "index.html"))
"""


# Initialisation de SQLite au démarrage
@app.on_event("startup")
def startup():
    init_db()

# Configuration CORS pour autoriser le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routes Authentification ---

@app.post("/api/auth/register")
def register(data: UserRegister):
    user = create_user(data.email, data.username, data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Cette adresse email est déjà utilisée.")
    return AuthResponse(
        token=user["token"],
        user=UserProfile(id=user["id"], email=user["email"], username=user["username"], xp=user["xp"])
    )

"""
@app.post("/api/auth/login")
def login(data: UserLogin):
    user = authenticate_user(data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect.")
    return AuthResponse(
        token=user["token"],
        user=UserProfile(id=user["id"], email=user["email"], username=user["username"], xp=user["xp"])
    )
"""

@app.post("/api/auth/login")
def login(data: UserLogin):
    user = authenticate_user(data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect.")
    return AuthResponse(
        token=user["token"],
        user=UserProfile(id=user["id"], email=user["email"], username=user["username"], xp=user["xp"])
    )


@app.get("/api/auth/me")
def get_me(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Non autorisé.")
    token = authorization.replace("Bearer ", "")
    user = get_user_by_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Session expirée.")
    return UserProfile(
        id=user["id"],
        email=user["email"],
        username=user["username"],
        xp=user["xp"]
    )


# --- Routes Curriculum & Exercices ---

@app.get("/api/curriculum/structure")
def get_curriculum_structure(authorization: Optional[str] = Header(None)):
    user_scores = {}
    if authorization:
        user = get_user_by_token(authorization.replace("Bearer ", ""))
        if user:
            user_scores = get_user_scores(user["id"])

    structure = {}
    for lvl_code, lvl_data in CURRICULUM_DB.items():
        categories = {}
        for cat_code, cat_data in lvl_data["categories"].items():
            ex_list = []
            for ex in cat_data["exercises"]:
                best_sc = user_scores.get(ex["id"], None)
                ex_list.append({
                    "id": ex["id"],
                    "title": ex["title"],
                    "questions_count": len(ex["questions"]),
                    "best_score": best_sc,
                    "is_passed": (best_sc is not None and best_sc >= 5.0)
                })
            categories[cat_code] = {
                "title": cat_data["title"],
                "exercises": ex_list
            }
        structure[lvl_code] = {
            "title": lvl_data["title"],
            "categories": categories
        }
    return structure

@app.get("/api/exercise/{exercise_id}")
def get_exercise(exercise_id: str):
    for lvl in CURRICULUM_DB.values():
        for cat in lvl["categories"].values():
            for ex in cat["exercises"]:
                if ex["id"] == exercise_id:
                    sanitized_q = [
                        {
                            "id": q["id"],
                            "type": q["type"],
                            "question": q["question"],
                            "options": q.get("options"),
                            "xp": q["xp"]
                        }
                        for q in ex["questions"]
                    ]
                    return {"id": ex["id"], "title": ex["title"], "questions": sanitized_q}
    raise HTTPException(status_code=404, detail="Exercice introuvable")

class FinishExercisePayload(BaseModel):
    exercise_id: str
    score_out_of_10: float

@app.post("/api/exercise/finish")
def finish_exercise(payload: FinishExercisePayload, authorization: Optional[str] = Header(None)):
    if authorization:
        user = get_user_by_token(authorization.replace("Bearer ", ""))
        if user:
            save_exercise_score(user["id"], payload.exercise_id, payload.score_out_of_10)
            return {"status": "saved", "best_score": payload.score_out_of_10}
    return {"status": "guest_ignored"}

@app.post("/api/validate", response_model=ValidationResult)
def validate_answer(submission: AnswerSubmission, authorization: Optional[str] = Header(None)):
    # Cherche la question dans CURRICULUM_DB ou QUESTIONS_DB
    question = None
    if "QUESTIONS_DB" in globals() and QUESTIONS_DB:
        question = next((q for q in QUESTIONS_DB if q["id"] == submission.question_id), None)
    
    if not question:
        for lvl in CURRICULUM_DB.values():
            for cat in lvl["categories"].values():
                for ex in cat["exercises"]:
                    for q in ex["questions"]:
                        if q["id"] == submission.question_id:
                            question = q
                            break

    if not question:
        raise HTTPException(status_code=404, detail="Question non trouvée.")

    is_correct = (normalize_text(submission.user_answer) == normalize_text(question["correct_answer"]))
    xp_to_award = question["xp"] if is_correct else 0
    current_total_xp = 0

    if authorization:
        user = get_user_by_token(authorization.replace("Bearer ", ""))
        if user and xp_to_award > 0:
            current_total_xp = add_user_xp(user["id"], xp_to_award)
        elif user:
            current_total_xp = user["xp"]

    return ValidationResult(
        is_correct=is_correct,
        correct_answer=question["correct_answer"],
        explanation=question.get("explanation", ""),
        xp_earned=xp_to_award,
        new_total_xp=current_total_xp
    )
def normalize_text(text: str) -> str:
    """Retire les accents, tildes, espaces superflus et met en minuscules."""
    if not text:
        return ""
    # Décompose les caractères avec accent (ex: ñ -> n + ~)
    nfkd = unicodedata.normalize('NFKD', text)
    # Supprime tous les signes diacritiques/accents
    cleaned = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return cleaned.strip().lower()