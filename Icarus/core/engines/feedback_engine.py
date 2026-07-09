"""
The `ICARUS` Complex Intent Engine

This file contains dependencies for ICARUS linked to responding to the user, either via speech or text.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from io import BytesIO
from pathlib import Path
from pydub import AudioSegment
from core.types import Response
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from durapy.src.uniCLI.uniCLI import Console
from core.utilities.decorators import runtime_log
from pydub.playback import play
from dotenv import load_dotenv
from os import environ

# Load API keys and models
load_dotenv(Path(__file__).resolve().parents[3] / ".env", verbose=True, encoding="utf-8")

# Initializers
elevenlabs = ElevenLabs(api_key=environ.get("ELEVENLABS_API_KEY"))

class FeedbackEngine:    
    @runtime_log
    def __init__(self, console: Console) -> None:
        """The Feedback Engine for ICARUS. This Engine handles speech, visualizations, and more."""
        
        console.start_task("Starting FeedbackEngine")
        
        # INIT LOGIC
        
        console.end_task("Starting FeedbackEngine", success=True)

    def __repr__(self):
        return f"FeedbackEngine()"

    @staticmethod
    def play_audio(audio_bytes: bytes) -> None:
        """Play the given audio bytes."""
        audio_buffer = BytesIO(audio_bytes)
        audio_segment = AudioSegment.from_file(audio_buffer)
        play(audio_segment)

    @runtime_log
    def speak(self, response: Response) -> None:
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
    
        audio_stream = BytesIO()
        for chunk in speech:
            if chunk:
                audio_stream.write(chunk)

        # Go to start of stream, play the stream and print the response.
        audio_stream.seek(0)
        self.play_audio(audio_stream.read())
        print(response)
        if "Goodbye" in response.text:
            exit(1)
  