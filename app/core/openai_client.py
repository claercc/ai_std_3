from functools import lru_cache

from openai import OpenAI
from app.core.config import Settings,get_settings



@lru_cache()
def get_openai_client() -> OpenAI:
    settings: Settings = get_settings()
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_api_base
    )
