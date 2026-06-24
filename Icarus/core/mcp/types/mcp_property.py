
from dataclasses import dataclass

@dataclass 
class MCPProperty:
    name: str
    dtype: type
    required: bool = True