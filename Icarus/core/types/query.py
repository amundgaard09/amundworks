
from durapy import uniCLI
from core.types.emotion_matrix import EmotionMatrix

class Query:
    """
    Query Class for representing a query from a user, with raw text and interpolated emotions.
    
    Args
    ----
        text (str): The raw text transcribed from the Perception Engine.
        emotions (EmotionMatrix): A representation of how ICARUS percieves the emotions of the user.
    """
    def __init__(self, text: str, emotions: EmotionMatrix) -> None:
        self.text = text.capitalize()
        self.emotions = emotions
    
    def __str__(self) -> str:
        return uniCLI.console_msg("USER", "green", f"{self.text}\n") #{self.emotions.__str__()}\n")
    
    def __repr__(self) -> str:
        return f"Query({self.text}, {self.emotions})"