import os
from dotenv import load_dotenv

from  pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


environment = os.getenv("ENVIRONMENT")

print(environment)

if environment == "development":
    print("Entorno de desarrollo")
elif environment == "production":
    print("Entorno de producción")

class Settings(BaseSettings):
    # Configuración de la app
    app_name: str 
    app_version: str
    app_description: str 
    app_author: str
    app_email: str
    environment: str
    debug: bool

model_config = SettingsConfigDict(env_file=".env")



class DevelopmentSettings(Settings):
    DEBUG: bool = True
    # DATABASE_URL: str = (
    #     f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
    #     f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
    # )
    # Imprimir para depuración
    # print(f"Development DATABASE_URL: {DATABASE_URL}")

class ProductionSettings(Settings):
    DEBUG: bool = False
    # DATABASE_URL: str = (
    #     f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
    #     f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
    # )

# Manejamos el entorno actual (development o production)
def get_settings() -> Settings:
    env = os.getenv("FASTAPI_ENV", "development")
    print(f"Running environment: {env}")
    if env == "production":
        return ProductionSettings()
    return DevelopmentSettings()


# Obtenemos la configuración actual
settings = get_settings()