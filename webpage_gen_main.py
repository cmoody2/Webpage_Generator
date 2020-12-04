#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.9.0
#
#   Author:         Christopher A. Moody
#
#   Purpose:        Create a webpage generator. Using tkinter, we will create
#                   a GUI that automates webpage creation and allows the user
#                   to tailor the webpage's content to their specification.
#                   This will be a simple webpage to demonstrate; use of tkinter
#                   functions, file handling operations and general OOP concepts.
#
#   Tested OS:      Written and tested with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import webpage_gen_gui
import webpage_gen_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,110)    #width,height
        self.master.maxsize(500,110)    #width,height

        webpage_gen_func.center_window(self, 500, 110)
        self.master.title("Webpage Generator")
        self.master.configure(bg="#F0F0F0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: webpage_gen_func.ask_quit(self))
        arg = self.master
        webpage_gen_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

        
