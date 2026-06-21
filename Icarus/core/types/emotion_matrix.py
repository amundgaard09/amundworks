"""
The EmotionMatrix class for the ICARUS Complex.
"""

from __future__ import annotations
from durapy import color_text as ct

class EmotionMatrix:
    def __init__(self):
        # Iteraction States
        self.empathy = 0.5
        self.patience = 1.0
        self.formality = 1.0
        
        # Cognitive Drives
        self.curiosity = 0.7
        self.skepticism = 0.3
        self.boredom = 0.0
        
        # Guardrail States
        self.caution = 0.5
        self.composure = 1.0
    
    def update(self, user_emotions: EmotionMatrix) -> None:
        pass
    
    def __str__(self):
        return f"[{ct(self.empathy, 'cyan')}][{ct(self.patience, 'pastel blue')}][{ct(self.formality, 'violet')}] - [{ct(self.curiosity, 'gold')}][{ct(self.skepticism, 'lime')}][{ct(self.boredom, 'gray')}] - [{ct(self.caution, 'red')}][{ct(self.composure, 'blue')}]"
