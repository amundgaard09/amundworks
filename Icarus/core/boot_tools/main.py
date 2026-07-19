
import subprocess
import platform

from typing import Callable
from durapy.src.uniCLI.uniCLI import Console, console_print
from core.utilities.decorators import runtime_log

def check_windows_wifi() -> bool:
    """Checks WiFi connectivity on Windows machines."""
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
        if "State" in output and "connected" in output.lower():
            return True

    except subprocess.CalledProcessError:
        pass

    except UnicodeDecodeError:
        console_print("ICARUS INITIALIZER", "red", "Wi-Fi check failed: UnicodeDecodeError", "yellow")

    return False

def check_linux_wifi() -> bool:
    """Checks WiFi connectivity on Linux machines."""
    try:
        output = subprocess.check_output("nmcli -t -f WIFI g", shell=True).decode().strip()
        return output == "enabled"

    except subprocess.CalledProcessError:
        pass

    except UnicodeDecodeError:
        console_print("ICARUS INITIALIZER", "red", "Wi-Fi check failed: UnicodeDecodeError", "yellow")

    return False

def check_macos_wifi() -> bool:
    """Checks WiFi connectivity on MacOS machines."""
    try:
        output = subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I", shell=True).decode()
        if "AirPort" in output and "state: running" in output.lower():
            return True

    except subprocess.CalledProcessError:
        pass

    except UnicodeDecodeError:
        console_print("ICARUS INITIALIZER", "red", "Wi-Fi check failed: UnicodeDecodeError", "yellow")

    return False

wifi_funcs: dict[str, Callable[[], bool]] = {
    "windows": check_windows_wifi,
    "linux": check_linux_wifi,
    "darwin": check_macos_wifi,
    "macos": check_macos_wifi
}

@runtime_log
def check_wifi(console: Console) -> None:
    """Check WiFi connectivity."""

    console.start_task("Checking Wi-Fi")

    # Get OS and wifi check function for that OS
    os = platform.system().lower()
    checkfunc = wifi_funcs.get(os, None)

    if checkfunc is None:
        console.end_task("Checking Wi-Fi", success=False, error_msg=f"Unknown OS: {os}")
        exit(-1)
    if not checkfunc():
        console.end_task("Checking Wi-Fi", success=False, error_msg="No active Wi-Fi connection found.")
        exit(-1)

    console.end_task("Checking Wi-Fi", success=True)

def check_microphone(console: Console) -> None:
    """Check if a microphone is available."""

    console.start_task("Checking Microphone")

    try:
        import sounddevice as sd
        devices = sd.query_devices()
        mic_available = any(device['max_input_channels'] > 0 for device in devices)

        if not mic_available:
            console.end_task("Checking Microphone", success=False, error_msg="No microphone detected.")
            exit(-1)

    except Exception as e:
        console.end_task("Checking Microphone", success=False, error_msg=f"Error checking microphone: {e}")
        exit(-1)

    console.end_task("Checking Microphone", success=True)
