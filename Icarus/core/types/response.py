
from core.types.emotion_matrix import EmotionMatrix
from durapy import uniCLI

class Response:
    def __init__(self, text: str, emotions: EmotionMatrix):
        self.text = text
        self.emotions = emotions
    
    def __str__(self):
        return uniCLI.console_msg("ICARUS", "blue", f"{self.text}\n") #{self.emotions.__str__()}\n")

    def __repr__(self):
        return f"Response({self.text}, {self.emotions})"
    
    def __getitem__(self, key):
        if key == "text" or key is None:
            return self.text
        elif key == "emotions":
            return self.emotions
        else:
            raise KeyError(f"Invalid key: {key}. Valid keys are 'text' and 'emotions'.")
    
    