from fastapi import FastAPI
from app.api.router import router

from app.domain.message import MessageRole, Message

msg = Message(role=MessageRole.USER, content="你好")



app = FastAPI(title="AI Agent Backend", version="0.1.0")
app.include_router(router)

if __name__ == "__main__":
    print(msg)
print(msg.model_dump())