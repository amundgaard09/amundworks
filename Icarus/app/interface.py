
from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Footer, Header, Button, Checkbox

class Dashboard(HorizontalGroup):
    """A Dashboard Widget for the ICARUS UI""" 
    
    def compose(self) -> ComposeResult:
        yield Button("Run ICARUS", id="start", variant="success")
        yield Button("Stop ICARUS", id="stop", variant="warning")
        yield Checkbox("Enable Camera", id="camera_toggle")
    
    def on_button_pressed(self):
        app.notify("Button pressed!")
    
    def on_checkbox_changed(self):
        app.notify("Checkbox changed!")
    
class IcarusUI(App):
    """The ICARUS User Interface"""
    
    CSS_PATH = "interface.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(Dashboard())
        yield Footer()
        
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    
if __name__ == "__main__":
    app = IcarusUI()
    app.run()