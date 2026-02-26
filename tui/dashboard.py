
from textual.app import App
from textual.widgets import Header,Footer,Static

class Dashboard(App):
    def compose(self):
        yield Header()
        yield Static("DevOps Enterprise Dashboard")
        yield Footer()

def launch_dashboard():
    Dashboard().run()
