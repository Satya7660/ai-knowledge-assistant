from app.providers.github_models import GitHubModelsProvider
from app.services.conversation_memory import ConversationMemory


class ChatService:

    def __init__(self):
        self.provider = GitHubModelsProvider()
        self.memory = ConversationMemory()

    def chat(self, message: str) -> str:

        self.memory.add_user_message(message)

        response = self.provider.chat(
            self.memory.get_messages()
        )

        self.memory.add_assistant_message(response)

        return response