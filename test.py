from vuipy.app import App
from vuipy.uix.label import Label


class MainApp(App):
    def __init__(self):
        super().__init__()
        
        label = Label()
        label.text = "hello vuipy!!!!!"
        
        self.window.append(label)


MainApp().run()
