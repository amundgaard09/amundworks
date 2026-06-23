
from dataclasses import dataclass

@dataclass
class IntentResult:
    """
    IntentResult Dataclass for Intent representation from `IntentEngine`
    
    Args
    ----
        intent (str): The derived intent (e.g.)
        confidence (float): The confidence on a scale from 0 - 100%.
        arguments (dict): Extracted arguments, sorted by type.
        source_text (str): The source text from the Query.
    """
    intent: str
    confidence: float
    arguments: dict
    source_text: str