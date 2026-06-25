"""
The `ICARUS` Complex Main Entrypoint.

This file contains the entrypoint for ICARUS.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from core.engines.intent_engine import IntentEngine

from core.engines.execution_engine import (
    initialize_execution as execution_init, 
    respond as EE_respond
)

from core.engines.feedback_engine import (
    initialize_feedback as feedback_init, 
    speak as FE_speak
)

from core.engines.perception_engine import (
    initialize_perception as perception_init, 
    listen as PE_listen
)

import subprocess, platform

from durapy import uniCLI
from core.utilities.exceptions import NotConnectedError, UnknownOSError
from core.utilities.decorators import logger

def check_windows_wifi() -> bool:
    """Checks WiFi connectivity on Windows machines."""
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode(encoding="utf-8", errors="strict")
        if "State" in output and "connected" in output.lower():
            return True
        
    except subprocess.CalledProcessError:
        pass
    
    except UnicodeDecodeError:
        uniCLI.console_print("ICARUS INITIALIZER: WARNING", "yellow", "WiFi Check failed: UnicodeDecodeError", "yellow")
    
    return False

wifi_check_funcs = {
    "windows": check_windows_wifi,
    "linux": None,
    "darwin": None, #MacOS
}

def get_os() -> str:
    """Returns the current operating system."""
    return platform.system().lower()
    
def check_wifi(debug: bool) -> None:
    """Check WiFi connectivity."""
    if debug: uniCLI.console_print("ICARUS INITIALIZER", "blue", "Checking Wi-Fi connection...")
    
    os = get_os()
    checkfunc = wifi_check_funcs.get(os, None)
    
    if checkfunc is None:
        raise UnknownOSError
    if not checkfunc():
        raise NotConnectedError

class IcarusInstance:
    @logger
    def __init__(self, debug: bool = False) -> None:
        """The main initializer function for ICARUS. This serves as a way to secure error-safe use of ICARUS."""
        if debug: uniCLI.console_print("ICARUS INITIALIZER", "blue", "Initializing Icarus...", "blue")
    
        check_wifi(debug=debug)
    
        perception_init(debug=debug)
        execution_init(debug=debug)
        feedback_init(debug=debug)

        if debug: uniCLI.console_print("ICARUS INITIALIZER", "blue", "Icarus Initialization Complete!", "green")

    listen = staticmethod(PE_listen)
    respond = staticmethod(EE_respond)
    speak = staticmethod(FE_speak)
    
@logger
def main(debug: bool) -> None:
    """The main dialouge kernel for the Icarus Complex"""
    try:
        Icarus = IcarusInstance(debug=debug)
        intent_engine = IntentEngine(debug=debug)
        
    except NotConnectedError:
        uniCLI.console_print("ICARUS", "red", "Icarus is not connected to the Internet. \n Exiting...", "red")
        exit(-1)
        
    except Exception as e:
        uniCLI.console_print("ICARUS", "blue", f"An error occured: {e}", "red")
        exit(-1)
    
    uniCLI.console_print("ICARUS", "blue", "Icarus Initialized\n", "green")
    
    while True:
        query = Icarus.listen()
        call = intent_engine.process(query)
        response = Icarus.respond(call)
        Icarus.speak(response) 
        if "Goodbye" in response.text:
            exit(1)

if __name__ == "__main__":
    main(debug=False)
