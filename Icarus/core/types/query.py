
from core.types.emotion_matrix import EmotionMatrix

class Query:
    """A intermediate representation of a user query"""
    def __init__(self, text: str, emotions: EmotionMatrix, toi: list[str]):
        self.text = text
        self.emotions = None
        self.toi = None # Tokens of interest: arguments, etc
    
    def __str__(self):
        pass