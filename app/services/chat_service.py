import app
from app.providers.github_models import GitHubModelsProvider
from app.services.conversation_memory import ConversationMemory
from app.core.constants import USER_ROLE, ASSISTANT_ROLE, SYSTEM_ROLE

class ChatService:

    def __init__(self):
        self.provider = GitHubModelsProvider()
        self.memory = ConversationMemory()

    def chat(self, session_id: str, message: str) -> str:

        self.memory.add_message(session_id, USER_ROLE, message)

        response = self.provider.chat(
            self.memory.get_messages(session_id)
        )

        self.memory.add_message(session_id, ASSISTANT_ROLE, response)

        return response