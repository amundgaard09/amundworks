"""
The `ICARUS` Complex Perception Engine

This file contains dependencies for ICARUS linked to perception, aka. listening and taking in text inputs.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from json import loads
from pathlib import Path
from queue import Queue

from durapy.durapy.uniCLI.uniCLI import Console, console_print
from sounddevice import PortAudioError, RawInputStream
from vosk import KaldiRecognizer, Model

from src.types import EmotionMatrix, Query

from ..shared.decorators import runtime_log

# Path to Icarus folder
ROOT = Path(__file__).resolve().parents[2]

# Load API keys and models
_SPEECH_MODEL_PATH = ROOT / "core" / "models" / "vosk-model-small-en-us-0.15"


class PerceptionEngine:
    @runtime_log
    def __init__(self, console: Console) -> None:
        """The ICARUS Perception Engine"""

        console.start_task("Starting PerceptionEngine")

        self.queue = Queue()
        self.model = Model(str(_SPEECH_MODEL_PATH))
        self.recognizer = KaldiRecognizer(self.model, 16000)

        console.end_task("Starting PerceptionEngine", success=True)

    def __repr__(self):
        return "PerceptionEngine()"

    def callback(self, indata, frames: int, time, status) -> None:
        self.queue.put(bytes(indata))

    @staticmethod
    def interpolate_emotions(text: str) -> EmotionMatrix:
        emotions = EmotionMatrix()
        return emotions  # placeholder for emotion interpolation

    @runtime_log
    def listen(self) -> Query:
        """Listen for speech with `sounddevice`.`RawInputStream()`. Part of the Perception Engine."""

        # Microphone input stream
        with RawInputStream(
            samplerate=16000,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=self.callback,
        ):
            try:
                while True:
                    # Get audio data from the queue
                    data = self.queue.get()

                    # Process the audio data with the recognizer
                    if self.recognizer.AcceptWaveform(data):
                        raw_result = self.recognizer.Result()
                        result_dict = dict(loads(raw_result))
                        result_text = str(result_dict.get("text", ""))
                        query = Query(
                            text=result_text,
                            emotions=self.interpolate_emotions(result_text),
                        )

                        print(query)
                        return query

            # Handle exceptions related to the audio input stream
            except PortAudioError as e:
                console_print(
                    "ICARUS PERCEPTION ENGINE",
                    "red",
                    f"An error occured: {e}",
                    "orange",
                )
                return Query(text="", emotions=EmotionMatrix())
