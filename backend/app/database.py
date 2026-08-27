import sqlite3
import hashlib
import secrets
from typing import Optional, Dict, Any
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "espagnol_app.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Table des utilisateurs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        xp INTEGER DEFAULT 0,
        token TEXT
    )
    """)
    # Table des questionnaires complétés sans faute
 # Table des scores (conserve le meilleur score sur 10)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_exercise_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        exercise_id TEXT NOT NULL,
        best_score REAL NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(user_id, exercise_id),
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)
    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def create_user(email: str, username: str, password: str) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    pwd_hash = hash_password(password)
    token = secrets.token_hex(24)
    try:
        cursor.execute(
            "INSERT INTO users (email, username, password_hash, xp, token) VALUES (?, ?, ?, 0, ?)",
            (email.lower(), username, pwd_hash, token)
        )
        conn.commit()
        user_id = cursor.lastrowid
        return {"id": user_id, "email": email.lower(), "username": username, "xp": 0, "token": token}
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()

def authenticate_user(email: str, password: str) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    pwd_hash = hash_password(password)
    cursor.execute(
        "SELECT id, email, username, xp FROM users WHERE email = ? AND password_hash = ?",
        (email.lower(), pwd_hash)
    )
    row = cursor.fetchone()
    if row:
        token = secrets.token_hex(24)
        cursor.execute("UPDATE users SET token = ? WHERE id = ?", (token, row["id"]))
        conn.commit()
        conn.close()
        return {"id": row["id"], "email": row["email"], "username": row["username"], "xp": row["xp"], "token": token}
    conn.close()
    return None

def get_user_by_token(token: str) -> Optional[Dict[str, Any]]:
    if not token:
        return None
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, username, xp FROM users WHERE token = ?", (token,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None

def add_user_xp(user_id: int, xp_to_add: int) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET xp = xp + ? WHERE id = ?", (xp_to_add, user_id))
    conn.commit()
    cursor.execute("SELECT xp FROM users WHERE id = ?", (user_id,))
    new_xp = cursor.fetchone()["xp"]
    conn.close()
    return new_xp

"""
def mark_quiz_completed(user_id: int, quiz_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO completed_quizzes (user_id, quiz_id) VALUES (?, ?)",
        (user_id, quiz_id)
    )
    conn.commit()
    conn.close()

def get_user_completed_quizzes(user_id: int) -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT quiz_id FROM completed_quizzes WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [r["quiz_id"] for r in rows]
    """

def save_exercise_score(user_id: int, exercise_id: str, score: float):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_exercise_scores (user_id, exercise_id, best_score)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id, exercise_id) 
        DO UPDATE SET best_score = MAX(best_score, excluded.best_score), updated_at = CURRENT_TIMESTAMP
    """, (user_id, exercise_id, score))
    conn.commit()
    conn.close()

def get_user_scores(user_id: int) -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT exercise_id, best_score FROM user_exercise_scores WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return {r["exercise_id"]: r["best_score"] for r in rows}