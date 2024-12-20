# Tesla Support API

> ⚠️ **Huge Disclaimer:** Every artifact (Ex: code, files, folders, documentation, etc.) was created following the instructions from [Cursor AI](https://www.cursor.so) **in less than 3 hours** by just doing **copy and paste**, and I don't even know Python! My request was - "Create a Python project following the instructions from https://github.com/cloudhumans/take-home" and here we are.

This is an implementation of the Cloud Humans take-home challenge, creating an AI-powered customer support API for Tesla Motors.

## Technical Decisions

1. **FastAPI Framework**: Chosen for its modern features, automatic OpenAPI documentation, and excellent async support.
2. **RAG Implementation**: Uses OpenAI's embedding model for vectorization and Azure AI Search for vector storage/retrieval.
3. **Smart Handover Feature**: Implements Option 2, automatically escalating N2-type content to human agents.
4. **Modular Design**: Services are separated into distinct modules for better maintainability and testing.

## Setup Instructions

1. Clone the repository
2. Create a `.env` file with:
```env
OPENAI_API_KEY=your_key_here
AZURE_AI_SEARCH_KEY=your_key_here
```

### Running with Docker:

```bash
docker build -t tesla-support-api .
docker run -p 8000:8000 --env-file .env tesla-support-api
```

### Running locally:

```bash
# 1. Navigate to the project directory
cd your-project-name

# 2. Create a virtual environment (PS: py_env is just an example name, change as you like)
python -m venv py_env

# 3. Activate the virtual environment (The source is your named env)
# On Windows:
py_env\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install the dependencies
pip install -r requirements

# 5. Run the application
uvicorn main:app --reload

# (Extra) - Use deactivate command to disable the virtual environment after the work is done ;)
deactivate

```


> Tip: you can also use `make` since we configured everything on Makefile to facilitate

## API Documentation

Access the API documentation at:
- http://localhost:8000/docs
- http://localhost:8000/redoc

## Future Improvements

1. Add request/response validation
2. Implement conversation history tracking
3. Add rate limiting and caching
4. Implement proper error handling
5. Add unit and integration tests
6. Add monitoring and logging

This implementation:
1. Uses RAG by combining OpenAI embeddings with Azure AI Search
1. Implements the Smart Handover feature (Option 2)
1. Follows modern Python practices and clean architecture
1. Is containerized for easy deployment
1. Includes comprehensive documentation