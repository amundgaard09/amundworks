
import time

def _get_formatted_time() -> str:
    return time.strftime("%H %M")

def execute() -> str:
    return f"The time is {_get_formatted_time()}"
