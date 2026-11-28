from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_extensions: list[str]
    max_upload_size: int
    tokenizer_model: str

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
    )


settings = Settings()
