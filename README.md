<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>

<p align="center">
  <img alt="Static Badge" src="https://img.shields.io/badge/python-3.12.7-green?logo=python">
  <img alt="Static Badge" src="https://img.shields.io/badge/fastapi-0.115.5-%23009485?logo=fastapi">
  <img alt="Static Badge" src="https://img.shields.io/badge/deepface-0.0.93-%238A2BE2?logo=deepface">
</p>

# Facial Recognition API

This application is a FastAPI-based API for facial recognition. It leverages advanced libraries like **DeepFace** for facial detection and verification.

## Requirements

- 🐍 Python 3.12.7 (or higher)

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/RamirezPineda/facial-recognition.git
cd facial-recognition
```

2. **Create a virtual environment:**
```bash
python -m venv .venv # Windows
python3 -m venv .venv # Linux/MacOS
```

3. **Activate a virtual environment:**
```bash
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/MacOS
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
fastapi dev app/main.py
```

**Access the interactive documentation:**
- Swagger: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc


## Project Structure
```
app/
├── common/
│   ├── constants/
│       └── endpoints.py
├── config/
│   └── env_config.py
├── recognition/
│   ├── controllers/
│   │   └── recognition_controller.py
│   ├── services/
│   │   └── recognition_service.py
│   ├── routes/
│       └── recognition_routes.py
├── main.py
└── routes.py
```
