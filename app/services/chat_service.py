from app.providers.github_models import GitHubModelsProvider


class ChatService:
    def __init__(self):
        self.provider = GitHubModelsProvider()

    def chat(self, message: str) -> str:
        return self.provider.chat(message)