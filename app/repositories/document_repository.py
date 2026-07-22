import sqlite3
from pathlib import Path
from datetime import datetime


class DocumentRepository:
    def __init__(self):
        self.database_path = Path("app/data/assistant.db")

        self.database_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self._create_tables()

    def _create_tables(self):
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT NOT NULL,
                    filepath TEXT NOT NULL,
                    uploaded_at TEXT NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS document_chunks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    document_id INTEGER NOT NULL,
                    chunk_text TEXT NOT NULL,
                    embedding TEXT,
                    FOREIGN KEY(document_id)
                        REFERENCES documents(id)
                        ON DELETE CASCADE
                )
            """)

            connection.commit()

    def create_document(self, filename: str, filepath: str):
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO documents(filename, filepath, uploaded_at)
                VALUES (?, ?, ?)
            """, (
                filename,
                filepath,
                datetime.now().isoformat()
            ))

            connection.commit()

            return cursor.lastrowid

    def get_document(self, document_id: int):
        with sqlite3.connect(self.database_path) as connection:
            connection.row_factory = sqlite3.Row

            cursor = connection.cursor()

            cursor.execute("""
                SELECT *
                FROM documents
                WHERE id = ?
            """, (document_id,))

            row = cursor.fetchone()

            return dict(row) if row else None

    def list_documents(self):
        with sqlite3.connect(self.database_path) as connection:
            connection.row_factory = sqlite3.Row

            cursor = connection.cursor()

            cursor.execute("""
                SELECT *
                FROM documents
                ORDER BY uploaded_at DESC
            """)

            return [dict(row) for row in cursor.fetchall()]

    def delete_document(self, document_id: int):
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                DELETE FROM documents
                WHERE id = ?
            """, (document_id,))

            connection.commit()