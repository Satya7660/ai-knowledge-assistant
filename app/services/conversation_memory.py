from app.core.prompts import SYSTEM_PROMPT


class ConversationMemory:

    def __init__(self):
        self._messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

    def add_user_message(self, message: str):
        self._messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(self, message: str):
        self._messages.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def get_messages(self):
        return self._messages

    def clear(self):
        self._messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]