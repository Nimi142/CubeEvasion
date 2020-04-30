from tkinter import *


class mycheckbox:
    def __init__(self, root, txt, offValue=0, onValue=1):
        self.__var = IntVar()
        self.widget = Checkbutton(root, text=txt, variable=self.__var, onvalue=onValue, offvalue=offValue)
        self.text = txt
        self.root = root

    def update(self):
        self.widget = Checkbutton(self.root, text=self.text, var=self.__var)

    def getVar(self):
        return self.__var.get()

    def pack(self):
        self.widget.pack()
