"""
Custom Types for the ICARUS Complex

Types
-----
- **EmotionMatrix** - An emotion representation for both ICARUS and the user.
- **Query** - Class for queries from the user.
- **Response** - Class for responses from ICARUS.
- **ToolCall** - A representation of what the user wants to do along with the given arguments. Acts as an Intermediate Representation between a query and a response.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from .emotion_matrix import EmotionMatrix
from .query import Query
from .response import Response
from .tool_call import ToolCall

__all__ = [
    "EmotionMatrix",
    "ToolCall",
    "Query",
    "Response"
]