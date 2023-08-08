# app.py
from fastapi import FastAPI,Form
from pydantic import BaseModel
# to avoid CORS errors when running locally
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from llm import Server


origins = [
    "http://localhost",
    "http://localhost:8080",
]
# cors middleware



app = FastAPI(
    title = "Server-LLM",
    version = '0.0.1'
)

account_sid = 'ACfa39038985b6e8ad6aa4baee0b74c422'
auth_token = 'a07e8e593d0fc86c5998faccf3661695'
client = Client(account_sid, auth_token)


app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Item(BaseModel):
    text : str
    
@app.post('/chat')
async def chat(request: Request):
    data = await request.form()
    twiml_response = MessagingResponse()
    twiml_response.message(get_response(data.get("Body")))
    return Response(content=str(twiml_response), media_type='application/xml')

def get_response(query: str):
    return server.get_answer(query)
    
@app.post('/')
async def chat(item : Item):
    return get_response(item.text)
    
# Get Data as a form and return response

server = Server()
server.load_pinecone()  