from dotenv import load_dotenv
import os

PYENV = os.getenv("PYENV", "dev")

load_dotenv(f".env.{PYENV}")
load_dotenv()

print(os.getenv("OPENAI_KEY"))
