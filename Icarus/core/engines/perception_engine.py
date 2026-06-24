"""
The `ICARUS` Complex Perception Engine

This file contains dependencies for ICARUS linked to perception, aka. listening and taking in text inputs.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

import json, queue, sounddevice

from pathlib import Path
from durapy import uniCLI
from vosk import Model, KaldiRecognizer
from core.types import Query, EmotionMatrix
from core.utilities.decorators import logger

# Path to Icarus folder
ROOT = Path(__file__).resolve().parents[2]

# Load API keys and models
_SPEECH_MODEL_PATH = ROOT / "core" / "models" / "vosk-model-small-en-us-0.15"

# Initializers
_queue = queue.Queue()
model = Model(str(_SPEECH_MODEL_PATH))
recognizer = KaldiRecognizer(model, 16000)

def callback(indata, frames: int, time, status) -> None:
    _queue.put(bytes(indata))

def interpolate_emotions(text: str) -> EmotionMatrix:
    emotions = EmotionMatrix()
    return emotions #placeholder for emotion interpolation

@logger   
def listen() -> Query:
    """Listen for speech with `sounddevice`.`RawInputStream()`. Part of the Perception Engine."""
    with sounddevice.RawInputStream(
        samplerate=16000, 
        blocksize=8000, 
        dtype="int16", 
        channels=1, 
        callback=callback
    ):
        try:
            while True:
                data = _queue.get()
                if recognizer.AcceptWaveform(data):
                    raw_result = recognizer.Result()
                    result_dict = dict(json.loads(raw_result))
                    result_text = str(result_dict.get("text", ""))
                    query = Query(
                        text=result_text,
                        emotions=interpolate_emotions(result_text),
                    )
                    
                    print(query)
                    return query
                
        except sounddevice.PortAudioError as e:
            uniCLI.console_print("ICARUS PERCEPTION ENGINE", "red", f"An error occured: {e}", "orange")

@logger
def initialize_perception(debug: bool) -> None:
    """Placeholder for future init logic for the Perception Engine."""
    if debug: 
        uniCLI.console_print("ICARUS", "blue", "Initializing Icarus Perception Engine...", "white")
        uniCLI.console_print("ICARUS", "blue", "Success!", "green")