import ctypes
import threading

from vuipy.uix.label import Label


class App(object):
    def __init__(self):
        self.lib = ctypes.cdll.LoadLibrary("./vuipy/lib/app.so")
        self.app = self.lib.vuipy__app()

        label = Label()
        print(label)
        label.text = "hello world"
        #self._widget_append(label)

    def run(self):
        print("run")
        self.lib.vuipy__run(self.app)
        #threading.Thread(target=self.runrun).start()
        print("end")
        #self.lib.vuipy__set_title(self.app)

    def _widget_append(self,widget):
        self.lib.vuipy__add_widget(self.app, widget.view)

    def runrun(self):
        self.lib.vuipy__run(self.app)
