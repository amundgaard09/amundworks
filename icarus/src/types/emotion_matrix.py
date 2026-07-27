"""
The EmotionMatrix class for the ICARUS Complex.
"""

from __future__ import annotations

from durapy import color_text as ct

from ..utilities.exceptions import UnknownEmotionError


class EmotionMatrix:
    def __init__(
        self,
        empathy: float = 0.5,
        patience: float = 1.0,
        formality: float = 1.0,
        curiosity: float = 0.7,
        skepticism: float = 0.3,
        boredom: float = 0.0,
        caution: float = 0.5,
        composure: float = 1.0,
    ):
        # Iteraction States
        self.empathy = empathy
        self.patience = patience
        self.formality = formality

        # Cognitive Drives
        self.curiosity = curiosity
        self.skepticism = skepticism
        self.boredom = boredom

        # Guardrail States
        self.caution = caution
        self.composure = composure

    def update(self, user_emotions: EmotionMatrix) -> None:
        """Updates Icarus' emotions based on the precieved emotions of the user."""
        pass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EmotionMatrix):
            return NotImplemented

        return (
            self.empathy == other.empathy
            and self.patience == other.patience
            and self.formality == other.formality
            and self.curiosity == other.curiosity
            and self.skepticism == other.skepticism
            and self.boredom == other.boredom
            and self.caution == other.caution
            and self.composure == other.composure
        )

    def __str__(self) -> str:
        return f"[{ct(self.empathy, 'cyan')}][{ct(self.patience, 'pastel blue')}][{ct(self.formality, 'violet')}] - [{ct(self.curiosity, 'gold')}][{ct(self.skepticism, 'lime')}][{ct(self.boredom, 'gray')}] - [{ct(self.caution, 'red')}][{ct(self.composure, 'blue')}]"

    def __repr__(self) -> str:
        return f"EmotionMatrix({self.empathy}, {self.patience}, {self.formality}, {self.curiosity}, {self.skepticism}, {self.boredom}, {self.caution}, {self.composure})"

    def __getitem__(self, key: str) -> float:
        match key:
            case "empathy":
                return self.empathy
            case "patience":
                return self.patience
            case "formality":
                return self.formality
            case "curiosity":
                return self.curiosity
            case "skepticism":
                return self.skepticism
            case "boredom":
                return self.boredom
            case "caution":
                return self.caution
            case "composure":
                return self.composure
            case _:
                raise UnknownEmotionError
