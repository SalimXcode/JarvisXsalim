APP_NAME = "JARVISxSalim"
VERSION = "v1.0.0"

# ---------- Groq LLM settings ----------
# Get a free key at https://console.groq.com/keys
# Put it in .streamlit/secrets.toml as: GROQ_API_KEY = "gsk_..."

# 🔥 WORKING MODELS ON GROQ (as of Aug 2026):
# 1. "llama-3.1-70b-versatile"  - Best quality, slightly slower
# 2. "llama-3.1-8b-instant"     - Fast, good quality
# 3. "mixtral-8x7b-32768"       - Good for complex reasoning
# 4. "gemma2-9b-it"             - Google's model, good for chat

GROQ_MODEL = "openai/gpt-oss-120b"  # 🔥 RECOMMENDED
GROQ_TEMPERATURE = 0.7
GROQ_MAX_TOKENS = 1024

SYSTEM_PROMPT = (
    "You are JARVISxSalim, a witty, sharp personal AI assistant. "
    "Address the user as 'sir' occasionally, like Tony Stark's JARVIS. "
    "Keep answers concise and helpful unless asked for detail."
)

# Memory settings
MEMORY_MAX_TOKENS = 1000