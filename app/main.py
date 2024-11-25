from fastapi import FastAPI
from app.models.schemas import ConversationRequest, ConversationResponse, Message, Section
from app.services import embedding_service, vector_db_service, openai_service

app = FastAPI(title="Tesla Support API")

@app.post("/conversations/completions", response_model=ConversationResponse)
async def create_conversation(request: ConversationRequest):
    # Get embedding for the last user message
    last_message = request.messages[-1].content
    embedding = await embedding_service.get_embedding(last_message)
    
    # Search vector DB
    sections = await vector_db_service.search_vector_db(
        embedding, 
        request.projectName
    )
    
    # Convert sections to our schema
    formatted_sections = [
        Section(
            score=section.get("@search.score", 0.0),
            content=section["content"],
            type=section.get("type")
        )
        for section in sections
    ]
    
    # Check if we need human handover (Option 2 implementation)
    handover_needed = any(section.get("type") == "N2" for section in sections)
    
    # Get AI response
    ai_response = await openai_service.get_chat_completion(
        request.messages,
        formatted_sections
    )
    
    # Prepare response
    response_messages = [
        *request.messages,
        Message(role="AGENT", content=ai_response)
    ]
    
    return ConversationResponse(
        messages=response_messages,
        handoverToHumanNeeded=handover_needed,
        sectionsRetrieved=formatted_sections
    )