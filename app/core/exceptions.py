class AIProviderException(Exception):
    """Raised when communication with the AI provider fails."""
    pass

class ConversationNotFoundException(Exception):
    """Raised when the requested conversation does not exist."""

    def __init__(self, session_id: str):
        super().__init__(
            f"Conversation '{session_id}' was not found."
        )