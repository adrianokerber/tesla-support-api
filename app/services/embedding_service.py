from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

async def get_embedding(text: str) -> list[float]:
    response = await client.embeddings.create(
        model="text-embedding-3-large",
        input=text
    )
    return response.data[0].embedding