"""
The `ICARUS` Complex Execution Engine

This file contains dependencies for ICARUS linked to execution of commands and tasks.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from durapy import uniCLI
from core.types.response import Response
from core.types.intent_result import IntentResult
from core.types.emotion_matrix import EmotionMatrix

def handle_unknown() -> str: # Add closest function system
    return "I didn't understand that." # Did you mean: etc...

def respond(IR: IntentResult) -> Response:
    """Return a `Response`-instance to the `Query`. Part of the Execution Engine."""
    func = None
    
    return Response(
        text=func() if func else handle_unknown(),
        emotions=EmotionMatrix()
    )
    
def initialize_execution(debug: bool) -> None:
    """Placeholder for future init logic for the Execution Engine."""
    if debug: 
        uniCLI.console_print("ICARUS", "blue", "Initializing Icarus Execution Engine...", "white")
        uniCLI.console_print("ICARUS", "blue", "Success!", "green")
