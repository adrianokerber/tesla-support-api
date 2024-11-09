.PHONY: install run clean test lint docker-build docker-run

# Install all dependencies
install:
	python3 -m venv py_env
	. py_env/bin/activate && pip install -r requirements

# Run the Tesla Support API locally
run:
	. py_env/bin/activate && uvicorn app.main:app --reload --port 8000 --host 0.0.0.0

# Clean up python cache and virtual environment
clean:
	rm -rf __pycache__
	rm -rf app/__pycache__
	rm -rf app/*/__pycache__
	rm -rf py_env
	find . -type f -name "*.pyc" -delete

# Build Docker image
docker-build:
	docker build -t tesla-support-api .

# Run Docker container
docker-run:
	docker run -p 8000:8000 --env-file .env tesla-support-api

# Stop all running containers
docker-stop:
	docker stop $$(docker ps -q --filter ancestor=tesla-support-api)

# Install dev dependencies and run tests
test:
	. py_env/bin/activate && pytest

# Check code style
lint:
	. py_env/bin/activate && flake8 .

# Create example environment file
env-example:
	echo "OPENAI_API_KEY=your_key_here" > .env.example
	echo "AZURE_AI_SEARCH_KEY=your_key_here" >> .env.example

# Setup complete development environment
setup: clean install env-example
	@echo "Setup complete. Remember to create your .env file!"