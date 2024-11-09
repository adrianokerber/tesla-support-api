from openai import AsyncOpenAI
from app.config import settings
from typing import List
from app.models.schemas import Message, Section

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

def create_system_prompt(sections: List[Section]) -> str:
    context = "\n".join([f"- {section.content}" for section in sections])
    return f"""You are Claudia, a Tesla support assistant. Be friendly and professional.
    Use ONLY the following information to answer questions:
    
    {context}
    
    If you cannot find relevant information to answer the question, ask for clarification.
    If you need to ask for clarification more than twice, inform the user that you'll need to transfer them to a human specialist.
    """

async def get_chat_completion(messages: List[Message], sections: List[Section]) -> str:
    system_prompt = create_system_prompt(sections)
    
    formatted_messages = [
        {"role": "system", "content": system_prompt},
        *[{"role": m.role.lower(), "content": m.content} for m in messages]
    ]
    
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=formatted_messages
    )
    
    return response.choices[0].message.content