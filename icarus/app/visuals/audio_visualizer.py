"""
The Speech Visualiser for ICARUS.

This module provides tools for visualizing ICARUS' speech.
"""

import sys

import numpy
import sounddevice
from PyQt5 import QtCore, QtWidgets

from durapy import uniCLI

app = QtWidgets.QApplication(sys.argv)

import pyqtgraph

# Audio Configuration Defaults
CHUNK_SIZE = 1024  # Number of audio frames per buffer
CHANNELS = 1  # Mono recording


class AudioVisualizer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Use PlotWidget as the central widget to avoid setCentralWidget crashes
        self.graphics_widget = pyqtgraph.PlotWidget(title="Live Audio Visualizer")
        self.setCentralWidget(self.graphics_widget)
        self.resize(800, 400)
        self.setWindowTitle("ICARUS Output Waveform Viewer")

        # Configure the plot inside the window container
        self.plot = self.graphics_widget
        self.plot.setTitle("Real-Time System Audio Output")
        self.plot.setYRange(-0.5, 0.5)  # Adjusted scaling for loopback audio
        self.plot.setXRange(0, CHUNK_SIZE)
        self.plot.showGrid(x=True, y=True)

        # Create a curve object with a styling color
        self.curve = self.plot.plot(pen=pyqtgraph.mkPen("c", width=2))

        # Internal buffer to store the active chunk of audio
        self.audio_data = numpy.zeros(CHUNK_SIZE)

        # Set up a thread-safe QTimer to refresh the UI at ~60 FPS
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(16)

        # Initialize the Windows WASAPI Loopback stream
        self.setup_windows_loopback()

    def setup_windows_loopback(self):
        """Locates the default Windows output device and hooks into its WASAPI loopback stream."""
        try:
            # 1. Locate the WASAPI host API index
            wasapi_idx = None
            for idx, api in enumerate(sounddevice.query_hostapis()):
                if "WASAPI" in api["name"]:
                    wasapi_idx = idx
                    break

            if wasapi_idx is None:
                raise RuntimeError("Windows WASAPI subsystem not found.")

            # 2. Get the default output device system info
            default_output_device = sounddevice.default.device[
                1
            ]  # Index 1 is default output
            output_info = sounddevice.query_devices(default_output_device)

            # 3. Find the corresponding WASAPI loopback device
            # WASAPI requires using the output device as an input device for loopback
            device_id = None
            for idx, device in enumerate(sounddevice.query_devices()):
                if (
                    device["hostapi"] == wasapi_idx
                    and device["max_output_channels"] > 0
                    and device["name"] == output_info["name"]
                ):
                    device_id = idx
                    break

            # Fallback if strict name matching fails
            if device_id is None:
                device_id = default_output_device

            # 4. Extract hardware sample rate (WASAPI strictly requires the native hardware rate)
            native_rate = int(
                sounddevice.query_devices(device_id)["default_samplerate"]
            )
            uniCLI.console_print(
                "ICARUS",
                "blue",
                f"Visualizing Audio From: {sounddevice.query_devices(device_id)['name']}",
            )
            uniCLI.console_print(
                "ICARUS", "blue", f"Hardware Sample Rate: {native_rate}Hz"
            )

            # 5. Spin up the stream using the output device as our input source
            self.stream = sounddevice.InputStream(
                channels=CHANNELS,
                samplerate=native_rate,
                blocksize=CHUNK_SIZE,
                device=device_id,
                callback=self.audio_callback,
            )
            self.stream.start()

        except Exception as e:
            uniCLI.console_print(
                "ICARUS", "red", f"Loopback initialization failed: {e}", "red"
            )
            uniCLI.console_print(
                "ICARUS",
                "blue",
                "Falling back to default system input device...",
                "yellow",
            )

            # Safe fallback to default microphone if loopback fails
            self.stream = sounddevice.InputStream(
                channels=CHANNELS,
                samplerate=44100,
                blocksize=CHUNK_SIZE,
                callback=self.audio_callback,
            )
            self.stream.start()

    def audio_callback(self, indata, frames, time, status):
        """This function is called by sounddevice in a separate thread for every new chunk."""
        if status:
            print(status, sys.stderr)
        # Flatten the input data array and save it to the buffer
        self.audio_data = indata[:, 0]

    def update_plot(self):
        """Updates the visual curve using data from the audio buffer."""
        self.curve.setData(self.audio_data)

    def close_event(self, event):
        """Cleans up the audio stream when the application window is closed."""
        if hasattr(self, "stream"):
            self.stream.stop()
            self.stream.close()
        event.accept()


if __name__ == "__main__":
    visualizer = AudioVisualizer()
    visualizer.show()
    sys.exit(app.exec_())
