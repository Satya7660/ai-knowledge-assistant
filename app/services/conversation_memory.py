from app.core.prompts import SYSTEM_PROMPT


class ConversationMemory:

    def __init__(self):
        self._conversations = {}

    def _ensure_conversation_exists(self, session_id: str):
        """Create a new conversation if it doesn't exist."""
        if session_id not in self._conversations:
            self._conversations[session_id] = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                }
            ]

    def add_user_message(self, session_id: str, message: str):
        self._ensure_conversation_exists(session_id)

        self._conversations[session_id].append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(self, session_id: str, message: str):
        self._ensure_conversation_exists(session_id)

        self._conversations[session_id].append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def get_messages(self, session_id: str):
        self._ensure_conversation_exists(session_id)
        return self._conversations[session_id]

    def clear(self, session_id: str):
        self._ensure_conversation_exists(session_id)
        self._conversations[session_id] = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]