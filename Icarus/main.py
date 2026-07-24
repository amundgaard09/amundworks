"""
The `ICARUS` Complex Main Entrypoint.

This file contains the entrypoint for ICARUS.

---

The ICARUS Complex is a Durendal project. More information can be found at the [Durendal GitHub](https://github.com/amundgaard09/durendal)
"""

from durapy import uniCLI

from src.boot_tools import check_microphone, check_wifi
from src.core import ExecutionEngine, FeedbackEngine, IntentEngine, PerceptionEngine
from src.mcp.mcp_server import MCPServer
from src.shared.decorators import runtime_log

Console = uniCLI.Console
clear_terminal = uniCLI.clear_terminal

class IcarusKernel:
    """The IcarusKernel class unifies all resources that ICARUS provides, such as NLP, computer vision, and more."""
    @runtime_log
    def __init__(self) -> None:

        clear_terminal()

        with Console() as console:
            console.start_task("Initializing Icarus")

            check_wifi(console)
            check_microphone(console)

            self.server = MCPServer(console)
            self.intent = IntentEngine(console, self.server)
            self.feedback = FeedbackEngine(console)
            self.execution = ExecutionEngine(console, self.server)
            self.perception = PerceptionEngine(console)

            console.end_task("Initializing Icarus", success=True)

@runtime_log
def main() -> None:
    """The main dialouge kernel for the Icarus Complex"""

    icarus = IcarusKernel()

    while True:
        query    = icarus.perception.listen()
        call     = icarus.intent.process(query)
        response = icarus.execution.respond(call)
        icarus.feedback.speak(response)

if __name__ == "__main__":
    main()
