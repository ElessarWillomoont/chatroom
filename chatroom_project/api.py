from typing import Union
from fastapi import FastAPI

from chatroom_project.models import MessageIn, MessageOut, ChatRoomIn, ChatRoomOut

app = FastAPI()

@app.post("/message/{room_id}", tags=['message'])
def post_a_message(room_id: str, message: MessageIn):
    return #TODO code this

@app.get("/message/{room_id}", tags=['message'])
def get_messages(room_id: str) -> ChatRoomOut:
    return None #TODO code that

@app.delete("/message/{message_id}", tags=['message'])
def delete_a_message(message_id: str):
    pass #TODO code this

@app.delete("/chatroom/{room_id}", tags=['chatroom'])
def delete_chatroom(room_id: str):
    pass #TODO code this

@app.post("/chatroom", tags=['chatroom'])
def create_a_chatroom(chatroom: ChatRoomIn):
    pass


