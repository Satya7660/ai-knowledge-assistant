from openai import OpenAI

from app.config.settings import settings


class GitHubModelsProvider:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.github_token,
            base_url=settings.base_url,
        )

    def chat(self, message: str) -> str:
        response = self.client.chat.completions.create(
            model=settings.model_name,
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
        )

        return response.choices[0].message.content