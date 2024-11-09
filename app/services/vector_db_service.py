import httpx
from app.config import settings

async def search_vector_db(vector: list[float], project_name: str) -> list[dict]:
    url = f"{settings.AZURE_SEARCH_ENDPOINT}/indexes/claudia-ids-index-large/docs/search?api-version=2023-11-01"
    
    payload = {
        "count": True,
        "select": "content, type",
        "top": 10,
        "filter": f"projectName eq '{project_name}'",
        "vectorQueries": [
            {
                "vector": vector,
                "k": 3,
                "fields": "embeddings",
                "kind": "vector"
            }
        ]
    }
    
    headers = {
        "Content-Type": "application/json",
        "api-key": settings.AZURE_AI_SEARCH_KEY
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        return response.json().get("value", [])