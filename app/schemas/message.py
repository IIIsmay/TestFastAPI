from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class MessageCreate(BaseModel):
    text: str = Field(min_length=1, max_length=5000)
    model_config = ConfigDict(str_strip_whitespace=True)


class MessageOut(BaseModel):
    id: int
    chat_id: int
    text: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
