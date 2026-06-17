"""
The ICARUS Complex System Core.

Engines
-------
The `engines` directory contains the three main systems of ICARUS. These are the communicative, intent, and execution engines.

MCP
---
The `MCP` directory manages the MCP system, like the server, tools, drivers, skills, etc.

Models
------
The `models` directory manages system models, like speech models and LLMs.

Utilities
---------
`Utilities` manages dependencies for ICARUS, such as runtime logging tools and package decorators.
"""

__all__ = ["engines", "mcp", "models", "utilities"]