from __future__ import annotations
from collections.abc import Iterator
from openai import OpenAI
from app.core.config import Settings
from app.domain.message import Message,MessageRole
from app.adapters.openai_message_adapter import OpenAIMessageAdapter
from app.services.conversation_service import ConversationService
from app.schemas.request import ChatRequest

class ChatService:
    """聊天服务"""

    def __init__(self, client: OpenAI,settings: Settings,conversation_service: ConversationService):
        self.client = client
        self.settings = settings
        self.conversation_service = conversation_service

    # def stream_chat(self, request: ChatRequest) -> Iterator[str]:
    #     """流式聊天"""
    #     raise NotImplementedError
    def chat(self, request: ChatRequest) -> str:
        """普通聊天"""
        conversation = self.conversation_service.get_or_create(request.session_id)
        conversation.add_message(Message(role=MessageRole.USER,content=request.message))
        response = self.client.chat.completions.create(
            model=self.settings.model_name,
            messages=OpenAIMessageAdapter.convert(conversation.get_messages()),
        )
        assistant_message = response.choices[0].message.content
        conversation.add_message(Message(role=MessageRole.ASSISTANT,content=assistant_message))
        self.conversation_service.save(conversation)
        return assistant_message
    
    def stream_chat(self, request: ChatRequest) -> Iterator[str]:
        """流式聊天"""
        conversation = self.conversation_service.get_or_create(request.session_id)
        conversation.add_message(Message(role=MessageRole.USER,content=request.message))
        response = self.client.chat.completions.create(
            model=self.settings.model_name,
            messages=OpenAIMessageAdapter.convert(conversation.get_messages()),
            stream=True
        )
        full_message = ""
        for chunk in response:
            context = chunk.choices[0].delta.content
            if context:
                full_message += context
                yield context
            conversation.add_message(Message(role=MessageRole.ASSISTANT,content=full_message))
            self.conversation_service.save(conversation)