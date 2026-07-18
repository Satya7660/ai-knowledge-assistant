from fastapi import APIRouter, HTTPException
from app.services.chat_service import ChatService
from app.core.exceptions import ConversationNotFoundException

router = APIRouter()

chat_service = ChatService()


@router.get("/conversations")
def get_conversations():
    return chat_service.get_conversations()

@router.get("/conversations/{session_id}")
def get_conversation(session_id: str):
    conversation = chat_service.get_conversation(session_id)

    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail=f"Conversation '{session_id}' was not found."
        )

    return conversation

@router.delete("/conversations/{session_id}")
def delete_conversation(session_id: str):
    deleted = chat_service.delete_conversation(session_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail=f"Conversation '{session_id}' was not found."
        )
    
    return {"message": f"Conversation '{session_id}' has been deleted."}