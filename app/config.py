from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    AZURE_AI_SEARCH_KEY: str
    AZURE_SEARCH_ENDPOINT: str = "https://claudia-db.search.windows.net"
    
    class Config:
        env_file = ".env"

settings = Settings()