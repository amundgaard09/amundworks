"""
The ICARUS Complex System Core.

Engines
-------
The `engines` directory contains the main systems of ICARUS. These are the preception, intent, execution and feedback engines.

MCP
---
The `MCP` directory manages the MCP system, like the server tools, drivers, skills, etc.

Models
------
The `models` directory manages system models, like speech models and LLMs.

Types
-----
The `types` directory contains custom classes such as `Response`, `IntentResult`, `Query`, etc.

Utilities
---------
`Utilities` manages dependencies for ICARUS, such as runtime logging tools and package decorators.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

__all__ = [
    "engines", 
    "mcp", 
    "models", 
    "types", 
    "utilities"
]