"""
The `ICARUS` Complex Main Entrypoint.

This file contains the entrypoint for ICARUS.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from core.engines.intent_engine import IntentEngine
from core.engines.execution_engine import ExecutionEngine
from core.engines.feedback_engine import FeedbackEngine
from core.engines.perception_engine import PerceptionEngine

import subprocess, platform

from durapy import uniCLI
from typing import Callable
from core.utilities.exceptions import NotConnectedError, UnknownOSError
from core.utilities.decorators import runtime_log

def check_windows_wifi() -> bool:
    """Checks WiFi connectivity on Windows machines."""
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode(encoding="utf-8", errors="strict")
        if "State" in output and "connected" in output.lower():
            return True
        
    except subprocess.CalledProcessError:
        pass
    
    except UnicodeDecodeError:
        uniCLI.console_print("ICARUS INITIALIZER: WARNING", "yellow", "Wi-Fi check failed: UnicodeDecodeError", "yellow")
    
    return False

wifi_check_funcs: dict[str, Callable[[], bool]] = {
    "windows": check_windows_wifi,
    "linux": None,
    "darwin": None, #MacOS
}

@runtime_log
def check_wifi(debug: bool) -> None:
    """Check WiFi connectivity."""
    if debug: uniCLI.console_print("ICARUS INITIALIZER", "blue", "Checking Wi-Fi connection...")
    
    # Get OS and wifi check function for that OS
    os = platform.system().lower()
    checkfunc = wifi_check_funcs.get(os, None)
    
    if checkfunc is None:
        raise UnknownOSError # Missing check function for given OS
    if not checkfunc():
        raise NotConnectedError # No wifi connection
    
    if debug: uniCLI.console_print("ICARUS INITIALIZER", "blue", "Wi-Fi connection established.", "green")

class IcarusInstance:
    @runtime_log
    def __init__(self, debug: bool = False) -> None:
        """The main initializer function for ICARUS"""
        
        if debug: uniCLI.console_print("ICARUS INITIALIZER", "blue", "Initializing Icarus...", "blue")

        try:
            check_wifi(debug=debug)
            
        except NotConnectedError:
            uniCLI.console_print("ICARUS", "red", "Icarus is not connected to the Internet. \n Exiting...", "red")
            exit(-1)
        
        except Exception as e:
            uniCLI.console_print("ICARUS", "blue", f"An error occured: {e}", "red")
            exit(-1)

        self.intent = IntentEngine(debug=debug)
        self.feedback = FeedbackEngine(debug=debug)
        self.execution = ExecutionEngine(debug=debug)
        self.perception = PerceptionEngine(debug=debug)

        if debug: uniCLI.console_print("ICARUS INITIALIZER", "blue", "Icarus Initialization Complete!", "green")
   
@runtime_log
def main(debug: bool) -> None:
    """The main dialouge kernel for the Icarus Complex"""
  
    Icarus = IcarusInstance(debug=debug)
        
    uniCLI.console_print("ICARUS", "blue", "Icarus Initialized\n", "green")
    
    while True:
        query    = Icarus.perception.listen()
        call     = Icarus.intent.process(query)
        response = Icarus.execution.respond(call)
        #Icarus.feedback.speak(response) 
        print(response)
        if "Goodbye" in response.text:
            exit(1)

if __name__ == "__main__":
    main(debug=False)
