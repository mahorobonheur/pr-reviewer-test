# user_service.py

import sqlite3
import hashlib


class UserService:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)

    def get_user(self, user_id: int) -> dict:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row is None:
            return {}
        return {"id": row[0], "name": row[1], "email": row[2]}

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def create_user(self, name: str, email: str, password: str) -> bool:
        hashed = self.hash_password(password)
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, hashed),
        )
        self.conn.commit()
        return True

    def close(self):
        self.conn.close()