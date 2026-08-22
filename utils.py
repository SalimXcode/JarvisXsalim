"""
utils.py - Helper functions (no TTS)
"""

import time
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def simulate_typing(text, placeholder, delay=0.03):
    full = ""
    for chunk in text.split():
        full += chunk + " "
        placeholder.markdown(full + "▌")
        time.sleep(delay)
    placeholder.markdown(text)