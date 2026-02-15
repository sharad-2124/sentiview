import os
from dotenv import load_dotenv

load_dotenv("config.env")

class Settings:

    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
    AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL_DEPLOYMENT_NAME")

    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

    BATCH_SIZE = 20
    SLEEP_SECONDS = 1
