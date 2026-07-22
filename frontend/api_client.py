import requests

class APIClient:
    def __init__(self):
        self.base_url = "http://localhost:8000"

    def chat(self, session_id: str, message: str):
        response = requests.post(
            f"{self.base_url}/chat",
            json={"session_id": session_id, "message": message},
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    
    def upload_document(self, uploaded_file):
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                uploaded_file.type
            )
    }
        response = requests.post(
            f"{self.base_url}/documents/upload",
            files=files,
            timeout=30
        )
        response.raise_for_status()
        return response.json()