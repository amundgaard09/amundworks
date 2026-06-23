"""
The `ICARUS` Complex Intent Engine

This file contains dependencies for ICARUS linked to responding to the user, either via speech or text.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

import io, os, dotenv
import pydub, pydub.playback as pd_playback

from core.types.response import Response
from core.types.query import Query
from core.utilities.decorators import logger
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from durapy import uniCLI
from pathlib import Path

# Load API keys and models
dotenv.load_dotenv(Path(__file__).resolve().parents[3] / ".env", verbose=True, encoding="utf-8")

# Initializers
elevenlabs = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))

def _play_audio(audio_bytes: bytes) -> None:
    """Play the given audio bytes."""
    audio_buffer = io.BytesIO(audio_bytes)
    audio_segment = pydub.AudioSegment.from_file(audio_buffer)
    pd_playback.play(audio_segment)

@logger
def speak(response: Response) -> None:
    """Speak the given text through `ElevenLabs` TTS. Also logs the text to the terminal. Part of the Feedback Engine."""
    speech = elevenlabs.text_to_speech.stream(
        voice_id="pNInz6obpgDQGcFmaJgB",
        output_format="mp3_22050_32",
        text=response.text,
        model_id="eleven_multilingual_v2",
        voice_settings = VoiceSettings(
            stability = 0.0,
            similarity_boost = 1.0,
            style = 0.0,
            use_speaker_boost = True,
            speed = 0.95,
        )
    )
    
    audio_stream = io.BytesIO()
    for chunk in speech:
        if chunk:
            audio_stream.write(chunk)

    # Go to start of stream, play the stream and print the response.
    audio_stream.seek(0)
    _play_audio(audio_stream.read())
    print(response)

@logger
def initialize_feedback(debug: bool) -> None:
    """Placeholder for future init logic for the Feedback Engine."""
    if debug: 
        uniCLI.console_print("ICARUS", "blue", "Initializing Icarus Feedback Engine...", "white")
        uniCLI.console_print("ICARUS", "blue", "Success!", "green")
