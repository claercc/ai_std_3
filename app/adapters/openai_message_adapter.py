from __future__ import annotations
from app.domain.message import Message

class OpenAIMessageAdapter:
    """OpenAI 消息适配器"""
    
    @staticmethod
    def convert(messages: list[Message]) -> list[dict]:
        """将消息列表转换为 OpenAI 消息格式"""
        return [
            {"role": msg.role.value, "content": msg.content}
            for msg in messages
        ]