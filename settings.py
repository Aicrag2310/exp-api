import logging
from functools import lru_cache
import pathlib
from pydantic import BaseSettings



SCRIPT_PATH = pathlib.Path(__file__).resolve().parent
LOCALES_DIR = SCRIPT_PATH.joinpath('locales')
EXP_API_DIR = SCRIPT_PATH.parent.parent

class Settings(BaseSettings):
    url_database: str
    

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()
