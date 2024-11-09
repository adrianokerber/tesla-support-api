from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    role: str
    content: str

class Section(BaseModel):
    score: float
    content: str
    type: Optional[str] = None

class ConversationRequest(BaseModel):
    helpdeskId: int
    projectName: str
    messages: List[Message]

class ConversationResponse(BaseModel):
    messages: List[Message]
    handoverToHumanNeeded: bool
    sectionsRetrieved: List[Section]