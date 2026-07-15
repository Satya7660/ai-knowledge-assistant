from app.core.prompts import SYSTEM_PROMPT
from app.repositories.conversation_repository import ConversationRepository

class ConversationMemory:

    def __init__(self):
        self._repository = ConversationRepository()

    def _ensure_conversation_exists(self, session_id: str):
        """Create a new conversation if it doesn't exist."""
        if not self._repository.conversation_exists(session_id):
            self._repository.create_conversation(session_id)

    def add_message(self, session_id: str, role: str, content: str):
        self._ensure_conversation_exists(session_id)
        self._repository.save_message(session_id, role, content)

    def get_messages(self, session_id: str):
        self._ensure_conversation_exists(session_id)
        return self._repository.get_messages(session_id)

    def clear(self, session_id: str):
        self._repository.clear_conversation(session_id)