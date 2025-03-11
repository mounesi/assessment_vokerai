import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set or invalid.")
else:
    print(f"Loaded OPENAI_API_KEY: {OPENAI_API_KEY[:5]}*****")  # Hide full key for security
