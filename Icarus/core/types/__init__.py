"""
Custom Types for the ICARUS Complex

Types
-----
- **EmotionMatrix** - An emotion representation for both ICARUS and the user.
- **IntentResult** - A representation of what the user wants to do along with the given arguments. Acts as an Intermediate Representation between a query and a response.
- **Query** - Class for queries from the user.
- **Response** - Class for responses from ICARUS.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

__all__ = [
    "emotion_matrix.py",
    "intent_result.py",
    "query.py",
    "response.py"
]