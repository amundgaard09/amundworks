
from core.types.emotion_matrix import EmotionMatrix
from durapy import uniCLI

class Response:
    def __init__(self, text: str, emotions: EmotionMatrix):
        self.text = text
        self.emotions = emotions
    
    def __str__(self):
        return uniCLI.console_msg("ICARUS", "blue", f"{self.text}\n{self.emotions.__str__()}")
