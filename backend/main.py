from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.router_agent import route_message
from agents.coding_agent import coding_agent
from agents.career_agent import career_agent
from agents.resume_agent import resume_agent
from agents.general_agent import general_agent


app = FastAPI(title="Multi-Agent Chatbot API")


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatMessage(BaseModel):
    role: str
    content: str
    agent: str | None = None


class ChatRequest(BaseModel):
    message: str
    history: list[ChatMessage] = [] 



@app.get("/")
def home():
    return {
        "message": "Multi-Agent Chatbot API is running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    agent = route_message(request.message, request.history)

    if agent == "coding":
        response = coding_agent(request.message, request.history)

    elif agent == "career":
        response = career_agent(request.message, request.history)

    elif agent == "resume":
        response = resume_agent(request.message, request.history)

    else:
        response = general_agent(request.message, request.history)

    return {
        "message": request.message,
        "agent": agent,
        "response": response
    }