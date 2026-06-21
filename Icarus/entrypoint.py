"""
The `ICARUS` Complex Main Entrypoint.

This file contains the entrypoint for ICARUS.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from core.engines.intent_engine import (
    initialize as intent_init
)

from core.engines.execution_engine import (
    initialize as execution_init, 
    respond
)

from core.engines.feedback_engine import (
    initialize as feedback_init, 
    speak
)

from core.engines.perception_engine import (
    initialize as perception_init, 
    listen
)

import subprocess
from core.utilities.exceptions import NotConnectedError
from core.utilities.decorators import logger
from durapy import uniCLI

def check_windows_wifi() -> bool:
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode("utf-8")
        if "State" in output and "connected" in output.lower():
            return True
    except subprocess.CalledProcessError:
        pass
    return False

@logger
def main_init(debug: bool) -> None:
    uniCLI.console_print("ICARUS INITIALIZER", "blue", "Initializing Icarus Engines...", "white")
    
    if not check_windows_wifi():
        raise NotConnectedError
    
    execution_init(debug)
    intent_init(debug)
    perception_init(debug)
    feedback_init(debug)
    
@logger
def main() -> None:
    """The main dialouge kernel for the Icarus Complex"""
    main_init(debug=False)
    
    uniCLI.console_print("ICARUS", "blue", "Listening...", "green")
    
    while True:
        input = listen()
        response = respond(input)
        speak(response) 
        if "Goodbye" in response.text:
            exit(1)

if __name__ == "__main__":
    main()
