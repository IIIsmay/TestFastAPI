import logging
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import select, desc

from app.core.db import get_db
from app.models import Chat, Message
from app.schemas.chat import ChatCreate, ChatOut, ChatWithMessagesOut
from app.schemas.message import MessageCreate, MessageOut

router = APIRouter()
log = logging.getLogger("api")


@router.post("/chats/", response_model=ChatOut, status_code=status.HTTP_201_CREATED)
def create_chat(payload: ChatCreate, db: Session = Depends(get_db)):
    chat = Chat(title=payload.title)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    log.info("Chat created id=%s", chat.id)
    return chat


@router.post("/chats/{chat_id}/messages/", response_model=MessageOut, status_code=status.HTTP_201_CREATED)
def send_message(chat_id: int, payload: MessageCreate, db: Session = Depends(get_db)):
    chat = db.get(Chat, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    msg = Message(chat_id=chat_id, text=payload.text)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    log.info("Message created id=%s chat_id=%s", msg.id, chat_id)
    return msg


@router.get("/chats/{chat_id}", response_model=ChatWithMessagesOut)
def get_chat_with_messages(
    chat_id: int,
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    chat = db.get(Chat, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    stmt = (
        select(Message)
        .where(Message.chat_id == chat_id)
        .order_by(desc(Message.created_at))
        .limit(limit)
    )
    last_messages = list(db.scalars(stmt).all())
    last_messages.reverse()

    return {
        "id": chat.id,
        "title": chat.title,
        "created_at": chat.created_at,
        "messages": last_messages,
    }


@router.delete("/chats/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
    chat = db.get(Chat, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    db.delete(chat)
    db.commit()
    log.info("Chat deleted id=%s", chat_id)
    return None
