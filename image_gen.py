"""
image_gen.py
------------
Free, keyless AI image generation via Pollinations.ai.
No signup, no API key. Rate-capped (~1 request / 15s on the anonymous tier),
and free-tier images may carry a small watermark — fine for a personal
project like this.

Docs: https://pollinations.ai
"""

import random
from urllib.parse import quote

import requests

BASE_URL = "https://image.pollinations.ai/prompt"

# Popular models available on Pollinations (subject to change on their end).
AVAILABLE_MODELS = ["flux", "turbo", "flux-realism", "flux-anime", "flux-3d"]


def generate_image(
    prompt: str,
    width: int = 1024,
    height: int = 1024,
    model: str = "flux",
    seed: int | None = None,
    nologo: bool = True,
    timeout: int = 60,
) -> bytes:
    """
    Generate an image from a text prompt via Pollinations.ai.

    Returns the raw image bytes (JPEG/PNG) on success.
    Raises requests.HTTPError / requests.Timeout on failure so the
    caller (Streamlit UI) can show a friendly error.
    """
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    if seed is None:
        seed = random.randint(0, 2_147_483_647)

    encoded_prompt = quote(prompt.strip())
    url = f"{BASE_URL}/{encoded_prompt}"

    params = {
        "width": width,
        "height": height,
        "model": model,
        "seed": seed,
        "nologo": str(nologo).lower(),
    }

    response = requests.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    return response.content