from fastapi import FastAPI
from chat_agent import chat
from data_models import ChatRequest, ChatResponse

app = FastAPI()


# Get Endpoint.........


@app.post("/chat", response_model=ChatResponse)
async def joke_chat(request: ChatRequest):
    chat_response = await chat(request)
    # Logic to store in database
    # ...
    
    return chat_response

