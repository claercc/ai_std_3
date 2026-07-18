from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    """聊天请求"""
    message: str = Field(description="用户消息",min_length=1)
    session_id: str = Field(description="会话ID",min_length=1)
