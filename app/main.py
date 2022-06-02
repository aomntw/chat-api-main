from app.module_login import login
from fastapi import FastAPI, Header, Form, Body
from pydantic import BaseModel


class ConversationUnit(BaseModel):
    text: str
    tag: str
    incoming_message: list
    outgoing_message: list
    created_at: str


class Service(BaseModel):
    name: str
    description: str
    version: str
    endpoint: str
    media_type: str
    parameter: list
    created_at: str


class incoming_message(BaseModel):
    session_id: str
    text: str
    context: dict


class outgoing_message(BaseModel):
    text: str
    context: dict


app = FastAPI()

app.include_router(login.router)


@app.get("/")
def read_root():
    return {"Hello": "Worldkkk"}
