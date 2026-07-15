import sqlite3
from pathlib import Path
from datetime import datetime


class ConversationRepository:

    def __init__(self):
        self.database_path = Path("app/data/conversation.db")

        self.database_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self._create_tables()

    def _create_tables(self):
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    session_id TEXT PRIMARY KEY,
                    created_at TEXT NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    FOREIGN KEY (session_id)
                        REFERENCES conversations(session_id)
                        ON DELETE CASCADE
                )
            """)

            connection.commit()

    def conversation_exists(self, session_id: str) -> bool:
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT 1 FROM conversations WHERE session_id = ?
            """, (session_id,))

            return cursor.fetchone() is not None
    
    def create_conversation(self, session_id: str):
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO conversations (session_id, created_at)
                VALUES (?, ?)
                """, 
                (
                session_id, 
                datetime.now().isoformat()
                )
            )
            connection.commit()

    def save_message(self, session_id: str, role: str, content: str):
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO messages (session_id, role, content, created_at)
                VALUES (?, ?, ?, ?)
            """, (session_id, role, content, datetime.now().isoformat()))

            connection.commit()

    def get_messages(self, session_id: str):
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT role, content FROM messages WHERE session_id = ?
                ORDER BY created_at ASC
            """, (session_id,))

            rows = cursor.fetchall()
            return [
            {
                "role": role,
                "content": content
            }
            for role, content in rows
            ]

    def clear_conversation(self, session_id: str):
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                DELETE FROM messages WHERE session_id = ?
            """, (session_id,))

            connection.commit()