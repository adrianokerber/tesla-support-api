from openai import AsyncOpenAI
from app.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)  # OpenAI client handles Bearer prefix

async def get_embedding(text: str) -> list[float]:
    response = await client.embeddings.create(
        model="text-embedding-3-large",
        input=text
    )
    return response.data[0].embedding