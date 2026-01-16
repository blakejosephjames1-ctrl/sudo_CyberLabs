from dotenv import dotenv_values
from pathlib import Path

backend_root = Path(__file__).parent.parent.parent
env_file = backend_root / ".env"
env_vars = dotenv_values(str(env_file)) if env_file.exists() else {}

class Settings:
    DATABASE_URL: str = env_vars.get("DATABASE_URL")
    SECRET_KEY: str = env_vars.get("SECRET_KEY")
    PROXMOX_API_URL: str = env_vars.get("PROXMOX_API_URL")


settings = Settings()
