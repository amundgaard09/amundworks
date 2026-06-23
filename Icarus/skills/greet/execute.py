"""
Get Time Skill
--------------
"""

import time, random

_GENERIC_GREETINGS = [
    "Hello, Simon!",
    "What's up, Simon?",
    ""
]

_EVENING_GREETINGS = [
    "Good evening, Simon!",
    "Good afternoon, Simon!"
]

_MORNING_GREETINGS = [
    "Good morning, Simon!"
]

def execute() -> str:
    current_time = (int(time.strftime("%H")), int(time.strftime("%M")))
    if current_time > (12, 00):
        return random.choice(_EVENING_GREETINGS + _GENERIC_GREETINGS)
    else:
        return random.choice(_MORNING_GREETINGS + _GENERIC_GREETINGS)
