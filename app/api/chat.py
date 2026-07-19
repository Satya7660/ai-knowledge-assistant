from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.core.exceptions import AIProviderException
from app.models.chat_models import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])

chat_service = ChatService()


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        response = chat_service.chat(
            request.session_id, 
            request.message
        )
        return ChatResponse(response=response)
        # return StreamingResponse(
        #     response,
        #     media_type="text/plain"
        # )
    
    except AIProviderException:
        raise HTTPException(
            status_code=503,
            detail="AI service is currently unavailable. Please try again later."
        )