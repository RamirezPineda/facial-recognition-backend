from dotenv import load_dotenv
import os

load_dotenv()


class EnvConfig:
    PORT = int(os.getenv("PORT", 8000))
