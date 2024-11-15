from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)


# Run a Server Manually
# Run the command
# uvicorn main:app --host 0.0.0.0 --port 80 --app-dir app

# OR

# import uvicorn
# from config.env_config import EnvConfig
# uvicorn.run(app, host="127.0.0.1", port=EnvConfig.PORT)
# Run the command
# python app/main.py # Windowns
# python3 app/main.py # Linux
