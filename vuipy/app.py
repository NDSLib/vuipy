import ctypes
import threading
import time

from vuipy.uix.label import Label


class App(object):
    def __init__(self):
        self.lib = ctypes.cdll.LoadLibrary("./vuipy/lib/app.so")
        self.app = self.lib.vuipy__app()

        #self.app.vuipy__test_p_call(self.test)

        self.window = []


    def test():
        print("test")

    def run(self):
        #label = Label()
        #label.text = "hello python!"
        #self.window.append(label)

        for item in self.window:
            self._widget_append(item.view)

        print("run")
        #self.lib.vuipy__run(self.app)
        threading.Thread(target=self.runrun).start()
        print("end")
        #self.lib.vuipy__test_label(self.app)
        #self.lib.vuipy__set_title(self.app)

    def _widget_append(self,widget):
        self.lib.vuipy__add_widget(self.app, widget)

    def runrun(self):
        self.lib.vuipy__run(self.app)
