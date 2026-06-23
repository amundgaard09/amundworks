"""
The `ICARUS` Complex Intent Engine

This file contains dependencies for ICARUS linked to figuring out what and how to do tasks.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

import re as regex

from durapy import uniCLI
from typing import Callable
from core.types.query import Query
from core.types.intent_result import IntentResult
from core.utilities.decorators import logger

def normalize(query: Query) -> Query:
    query.text = query.text.lower().strip()
    return query

@logger
def match(query: Query, trigger_map: dict) -> Callable[[], str] | None:
    """Extracts triggers from query and returns the most probable function."""
    query = normalize(query)

    for trigger in trigger_map: # Loop over all triggers (sentences) in the trigger map
        if trigger in query.text:
            return trigger_map[trigger] # Return function for given trigger

    return None

def extract_intent(query: Query) -> str:
    text = query.text.lower()

    if "time" in text or "clock" in text:
        return "get_time"

    if "calendar" in text:
        return "calendar_lookup"

    if "search" in text or "google" in text:
        return "web_search"

    return "unknown"

def extract_args(query: Query, intent: str) -> dict:
    text = query.text

    if intent == "math_sum":
        numbers = regex.findall(r"\d+", text)
        return {"numbers": list(map(int, numbers))}

    if intent == "web_search":
        return {"query": text}

    return {}
    
@logger
def process(query: Query) -> IntentResult:
    """Process a `Query` and return an `IntentResult`. Part of the Intent Engine."""
    intent = extract_intent(query)
    args = extract_args(query, intent)
    
    return IntentResult(
        intent=intent,
        confidence=0.0,
        arguments=args,
        source_text=query.text
    )

@logger
def initialize_intent(debug: bool) -> None:
    """Placeholder for future init logic for the Intent Engine."""
    if debug: 
        uniCLI.console_print("ICARUS", "blue", "Initializing Icarus Intent Engine...", "white")
        uniCLI.console_print("ICARUS", "blue", "Success!", "green")
        
        
# En enda bedre struktur (anbefalt)

#Du kan gjøre dette:

#class IntentSpec:
#    name: str > skill name
#    arg_parser: Callable -> Arg Extractor Func

#Og registry:

#INTENT_REGISTRY = {
#    "math_sum": IntentSpec(...),
#    "web_search": IntentSpec(...)
#}
