from pydantic_settings import BaseSettings


class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


class Env(Singleton, BaseSettings):
    mlflow_tracking_uri: str = "./mlruns"
    mlflow_registry_uri: str = "./mlruns"
    mlflow_experiment_name: str = "autogen_team"
    mlflow_registered_autogen_team: str = "autogen_team"

    class Config:
        case_sensitive = False  # Optional: make env var lookup case-insensitive
        env_file = ".env"  # Enable reading from .env file
        env_file_encoding = "utf-8"
