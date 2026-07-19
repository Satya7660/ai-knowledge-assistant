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

        # complete_response = ""
        # for chunk in response_stream:
        #     complete_response += chunk  
        #     yield chunk  # Yield each chunk as it arrives
        self.memory.add_message(session_id, ASSISTANT_ROLE, response)
        return response

    def get_conversations(self):
        return self.memory.get_conversations()
    
    def get_conversation(self, session_id: str):
        return self.memory.get_conversation(session_id)
    
    def delete_conversation(self, session_id: str):
        return self.memory.delete_conversation(session_id)