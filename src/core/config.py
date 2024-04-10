from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Store API"
    PROJECT_VERSION: str = "0.1.0"
    ROOT_PATH: str = "/"

    DB_HOST: str = ""
    DB_NAME: str = ""
    DB_USER: str = ""
    DB_PASS: str = ""

    # DATABASE_URL: str = ""

    model_config = SettingsConfigDict(env_File=".env")

    @property
    def DATABASE_URL(self) -> str:
        return f"mongodb+srv://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}?retryWrites=true&w=majority"


settings = Settings()
