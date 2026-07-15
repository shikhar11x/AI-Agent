BASE_URL = "https://api.groq.com/openai/v1"

MODEL_NAME = "llama-3.3-70b-versatile"
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")