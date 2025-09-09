import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def _get_hf_token() -> str | None:
    """Return the Hugging Face token from common environment names."""
    token = (
        os.getenv("HUGGINGFACEHUB_API_TOKEN")
        or os.getenv("HF_TOKEN")
        or os.getenv("HUGGINGFACE_API_KEY")
    )
    if token:
        # Ensure libraries that rely on the standard HF_TOKEN variable can find it.
        os.environ.setdefault("HF_TOKEN", token)
    return token


HUGGINGFACEHUB_API_TOKEN = _get_hf_token()
if not HUGGINGFACEHUB_API_TOKEN:
    raise ValueError(
        "❌ Hugging Face token not set. Please define HUGGINGFACEHUB_API_TOKEN, HF_TOKEN, or HUGGINGFACE_API_KEY."
    )
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "false")

DATA_DIR = "./data"
VECTOR_STORE_DIR = "./vector_index"
