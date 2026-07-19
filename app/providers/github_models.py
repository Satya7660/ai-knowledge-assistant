from openai import OpenAI
from app.config.settings import settings
from app.core.exceptions import AIProviderException
from app.core.prompts import SYSTEM_PROMPT

class GitHubModelsProvider:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.github_token,
            base_url=settings.base_url,
        )

    def chat(self, messages: list) -> str:
        try:
            response = self.client.chat.completions.create(
                model=settings.model_name,
                messages=messages,
                #stream=True
            )
            return response.choices[0].message.content
            # for chunk in response:
            #     print(chunk)

            #     if not chunk.choices:
            #         continue

            #     delta = chunk.choices[0].delta

            #     if delta.content:
            #         yield delta.content

        except Exception as e:
            raise AIProviderException(f"Failed to communicate with GitHub Models: {e}")
        