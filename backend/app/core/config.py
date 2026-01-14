import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    PROXMOX_API_URL: str = os.getenv("PROXMOX_API_URL")


settings = Settings()
