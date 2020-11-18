import ctypes

class Label:
    def __init__(self):
        self.__lib = ctypes.cdll.LoadLibrary("./vuipy/lib/app.so")
        self.__text = "Label"

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value


    @property
    def view(self):
        view = self.__lib.vuipy__label(self.__text)
        return view



