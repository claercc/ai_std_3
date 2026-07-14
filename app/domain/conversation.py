# conversation 对话

# Message
#         ↓
# Conversation
#         ↓
# ConversationRepository（接口）
#         ↓
# InMemoryConversationRepository（实现）
#         ↓
# ConversationService
#         ↓
# ChatService

from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from app.domain.message import Message

class Conversation(BaseModel):
    """一个完整的对话"""
    model_config = ConfigDict(from_attributes=True) #模型可以直接从具有相同字段名的任意对象中创建实例，而无需手动转换
    session_id: str = Field(description="会话ID")
    messages: list[Message] = Field(description="消息列表")

    def add_message(self, message: Message):
        """添加消息"""
        self.messages.append(message)
    
    def get_messages(self) -> list[Message]:
        """获取所有消息"""
        return self.messages.copy()
    
    def clear(self) -> None:
        """清空历史消息"""
        self.messages.clear()