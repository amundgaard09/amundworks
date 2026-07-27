
from dataclasses import dataclass

@dataclass
class ToolCall:
    """
    ToolCall Dataclass representing a tool call from `IntentEngine` to `ExecutionEngine`.
    
    Args
    ----
        tool_name (str): The tool name
        confidence (float): The confidence on a scale from 0 - 100%.
        arguments (dict): Extracted arguments, sorted by type.
        source_text (str): The source text from the Query.
    """
    tool_name: str
    confidence: float
    arguments: dict
    source_text: str