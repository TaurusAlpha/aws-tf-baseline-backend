# AWS Terraform Baseline Backend

Backend API for generating AWS Terraform baseline configuration files based on user input.

## Requirements

- Python 3.13+
- Docker (optional)

## Features

- FastAPI-based REST API
- Health check endpoints
- Docker containerization
- Async operations support
- Modern Python tooling (Black, Ruff, MyPy)

## Quick Start

### Local Development

1. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

2. Install dependencies using pip:
```bash
pip install -r requirements.txt
```

Or using the modern approach with pyproject.toml:
```bash
pip install -e ".[dev]"
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

4. Access the API documentation at: http://localhost:8000/docs

**Note for VSCode users:** After creating the virtual environment, VSCode should automatically detect it. If not, press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS), type "Python: Select Interpreter", and choose the interpreter from `.venv/bin/python`.

### Development Tools

Format code:
```bash
black .
isort .
```

Lint code:
```bash
ruff check .
```

Type checking:
```bash
mypy app/
```

### Docker

1. Build the image:
```bash
docker build -t aws-tf-baseline-backend .
```

2. Run the container:
```bash
docker run -p 8000:8000 aws-tf-baseline-backend
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check

## Testing

Run tests with:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=app tests/
```

## Technology Stack

- **Python 3.13** - Latest Python version
- **FastAPI 0.109+** - Modern async web framework
- **Pydantic 2.6+** - Data validation and serialization
- **Uvicorn** - ASGI server
- **Boto3** - AWS SDK for Python
