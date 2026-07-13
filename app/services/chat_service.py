from app.providers.github_models import GitHubModelsProvider
from app.core.prompts import SYSTEM_PROMPT

class ChatService:
    def __init__(self):
        self.provider = GitHubModelsProvider()

    def chat(self, message: str) -> str:
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": message,
            },
        ]
        return self.provider.chat(messages)