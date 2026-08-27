from pydantic import BaseModel, EmailStr
from typing import List, Optional

# --- Modèles d'authentification ---
class UserRegister(BaseModel):
    email: EmailStr
    username: str  # Le prénom / pseudo
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserProfile(BaseModel):
    id: int
    email: str
    username: str
    xp: int

class AuthResponse(BaseModel):
    token: str
    user: UserProfile

# --- Modèles Quiz ---
class QuestionResponse(BaseModel):
    id: int
    type: str
    question: str
    options: Optional[List[str]] = None
    xp: int

class AnswerSubmission(BaseModel):
    question_id: int
    user_answer: str

class ValidationResult(BaseModel):
    is_correct: bool
    correct_answer: str
    explanation: str
    xp_earned: int
    new_total_xp: int = 0
