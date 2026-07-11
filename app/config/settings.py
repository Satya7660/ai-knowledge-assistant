from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "AI Knowledge Assistant")
        self.debug = os.getenv("DEBUG", "False").lower() == "true"
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.model_name = os.getenv("MODEL_NAME", "gpt-4.1-mini")
        self.base_url = os.getenv(
            "BASE_URL",
            "https://models.inference.ai.azure.com"
        )

settings = Settings()

