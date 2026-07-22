from app.domain.conversation import Conversation
from app.domain.message import Message,MessageRole

class PromptBuilder:
    """负责构建发送给LLM的消息列表"""
    