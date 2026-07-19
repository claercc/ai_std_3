from fastapi import Depends
from app.api.router import router
from app.core.config import Settings,get_settings
from app.core.openai_client import get_openai_client
from app.repositories.memory_repository import MemoryConversationRepository
from app.services.chat_service import ChatService
from app.services.conversation_service import ConversationService
from app.schemas.request import ChatRequest
# stream chat
from collections.abc import Iterator



repository = MemoryConversationRepository()
def get_chat_service() -> ChatService:
    settings: Settings = get_settings()
    conversation_service = ConversationService(repository)
    return ChatService(
        client=Depends(get_openai_client),
        settings=settings,
        conversation_service=conversation_service
    )

@router.post("")
def chat(request: ChatRequest, chat_service: ChatService = Depends(get_chat_service)):
    answer = chat_service.chat(request)
    return {"answer": answer}

@router.post("/stream")
def stream_chat(request: ChatRequest, chat_service: ChatService = Depends(get_chat_service)) -> Iterator[str]:
    return chat_service.stream_chat(request)
