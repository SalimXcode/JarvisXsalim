import time
import asyncio
import edge_tts
import tempfile
import pygame
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

def speak(text):
    """Text-to-speech using Microsoft Edge Neural Voices (free, high quality)."""
    try:
        # ⭐ Change this voice to your preference
        VOICE = "en-US-JennyNeural"  # Female US voice - warm, natural
        
        # Other female options:
        # "en-US-AriaNeural"      - expressive, confident
        # "en-US-EmmaMultilingualNeural"  - multilingual, top-rated
        # "en-IN-NeerjaNeural"    - Indian English female
        # "en-GB-SoniaNeural"     - UK female
        # "en-US-MichelleNeural"  - friendly, clear
        
        async def _speak():
            # Generate speech to temp file
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                tmp_path = tmp.name
            
            communicate = edge_tts.Communicate(text, VOICE)
            await communicate.save(tmp_path)
            
            # Play using pygame
            pygame.mixer.init()
            pygame.mixer.music.load(tmp_path)
            pygame.mixer.music.play()
            
            # Wait for playback to finish
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            
            pygame.mixer.quit()
            
            # Cleanup temp file
            import os
            try:
                os.remove(tmp_path)
            except:
                pass
        
        # Run async function
        asyncio.run(_speak())
        
    except Exception as e:
        print(f"TTS error: {e}")