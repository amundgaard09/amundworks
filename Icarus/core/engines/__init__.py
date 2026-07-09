"""
The ICARUS Complex Engines Directory.

This directory contains the engines for ICARUS. These engines include:

The Perception Engine
---------------------
The Preception Engine handles ICARUS' senses, such as hearing and vision.  
This enables ICARUS to understand natural language via ElevenLabs and utilize computer vision via OpenCV.

The Execution Engine
--------------------
The Execution engine handles execution of functions parsed from the intent engine.

The Feedback Engine
-------------------
The Feedback Engine handles responses back to the user, such as speaking and other real world interactions.

The Intent Engine
-----------------
The Intent Engine handles the parsing of user queries. It extracts arguments and intent, and routes this to the execution engine.

---

ICARUS is a Durendal project. More information can be found at
"""

from .perception_engine import PerceptionEngine
from .execution_engine import ExecutionEngine
from .feedback_engine import FeedbackEngine
from .intent_engine import IntentEngine

__all__ = [
    "ExecutionEngine",
    "FeedbackEngine",
    "IntentEngine",
    "PerceptionEngine",
]