from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
GROQ_MODEL=os.getenv("GROQ_MODEL")
TEMPERATURE = 0.7
MAX_TOKENS = 1024

if not GROQ_API_KEY:
    raise ValueError("GROQ API KEY MESSING!!!")
if not GROQ_MODEL:
    raise ValueError("GROQ MODEL IS MESSING!")