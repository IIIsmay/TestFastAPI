from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class ChatCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    model_config = ConfigDict(str_strip_whitespace=True)


class ChatOut(BaseModel):
    id: int
    title: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class ChatWithMessagesOut(ChatOut):
    messages: list["MessageOut"]


from app.schemas.message import MessageOut  # noqa: E402

ChatWithMessagesOut.model_rebuild()
