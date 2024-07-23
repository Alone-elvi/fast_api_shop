from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    rabbitmq_host: str
    rabbitmq_port: int
    rabbitmq_management_port: int
    rabbitmq_queue: str

    class Config:
        env_file = ".env"

settings = Settings()
