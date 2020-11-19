import ctypes

class Label:
    def __init__(self):
        self.__lib = ctypes.cdll.LoadLibrary("./vuipy/lib/app.so")
        self.__text = "Label"
        self.__c_text = None

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
        self.__c_text = ctypes.c_char_p(value.encode())


    @property
    def view(self):
        view = self.__lib.vuipy__label(self.__c_text)
        return view



