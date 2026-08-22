"""
utils.py - TTS with edge-tts + Streamlit audio player
"""

import time
import asyncio
import tempfile
import os
import base64
from datetime import datetime
import streamlit as st

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def simulate_typing(text, placeholder, delay=0.03):
    full = ""
    for chunk in text.split():
        full += chunk + " "
        placeholder.markdown(full + "▌")
        time.sleep(delay)
    placeholder.markdown(text)


def speak(text):
    """
    Text-to-speech using edge-tts.
    Audio played via Streamlit's built-in audio player.
    """
    try:
        # Check edge-tts
        try:
            import edge_tts
        except ImportError:
            print("edge-tts not installed")
            return

        # Female voice
        VOICE = "en-US-JennyNeural"
        
        async def _speak():
            # Generate audio to temp file
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                tmp_path = tmp.name
            
            communicate = edge_tts.Communicate(text, VOICE)
            await communicate.save(tmp_path)
            
            # 🔥 STREAMLIT AUDIO PLAYER (works everywhere)
            with open(tmp_path, "rb") as f:
                audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/mp3", autoplay=True)
            
            # Cleanup
            try:
                os.remove(tmp_path)
            except:
                pass
        
        # Run async
        asyncio.run(_speak())
        
    except Exception as e:
        print(f"TTS error: {e}")