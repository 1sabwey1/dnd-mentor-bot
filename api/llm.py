import os

from dotenv import load_dotenv
from gigachat import GigaChat

load_dotenv()


async def ask_llm(question: str) -> str:
    async with  GigaChat(
        credentials=os.getenv("GIGACHAT_CREDENTIALS"),
        scope=os.getenv("GIGACHAT_SCOPE"),
        model=os.getenv('GIGACHAT_MODEL'),
        verify_ssl_certs=False,
    ) as giga:
        response =  await giga.achat(question)
        return response.choices[0].message.content
