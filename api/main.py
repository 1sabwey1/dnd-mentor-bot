from fastapi import FastAPI
from pydantic import BaseModel
from api.llm import ask_llm

app = FastAPI()

class AskRequest(BaseModel):
    question: str


@app.get('/health')
async def health():
    return {'status': 'ok'}


@app.post('/ask')
async def ask(request: AskRequest):
    answer = await ask_llm(request.question)
    return {'answer': answer}
