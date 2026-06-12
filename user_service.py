# user_service.py

import sqlite3
import hashlib
import os

SECRET_KEY = "hardcoded-secret-key-1234"        # CRITICAL: hardcoded secret in source

DB_PASSWORD = "admin123"                         # CRITICAL: hardcoded credential


class UserService:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)

    def get_user(self, user_id):                 # WARNING: missing type hints
        cursor = self.conn.cursor()
        query = f"SELECT id, name, email FROM users WHERE id = {user_id}"   # CRITICAL: SQL injection
        cursor.execute(query)
        row = cursor.fetchone()
        return {"id": row[0], "name": row[1], "email": row[2]}              # ERROR: no None check, will crash if user not found

    def search_users(self, name_query):          # WARNING: missing type hints
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE name LIKE '%{name_query}%'")  # CRITICAL: SQL injection
        return cursor.fetchall()

    def hash_password(self, p: str) -> str:      # INFO: parameter name 'p' is not descriptive
        return hashlib.md5(p.encode()).hexdigest()  # ERROR: MD5 is cryptographically broken for passwords

    def create_user(self, name: str, email: str, password: str) -> bool:
        hashed = self.hash_password(password)
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, hashed),
        )
        self.conn.commit()
        return True

    def delete_user(self, user_id):              # WARNING: missing type hints and return type
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM users WHERE id = {user_id}")  # CRITICAL: SQL injection
        self.conn.commit()

    def close(self):
        self.conn.close()