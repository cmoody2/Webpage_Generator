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

import webpage_gen_func
import webpage_gen_main


def load_gui(self):
    
    # buttons
    self.btn_clear = tk.Button(self.master, width=14, height=1, text='Clear Text', command=lambda: webpage_gen_func.onClear(self))
    self.btn_clear.grid(row=1, column=0, padx=(10,10), pady=(35,0), sticky=W)
    self.btn_create = tk.Button(self.master, width=14, height=1, text='Create Page', command=lambda: webpage_gen_func.create_file(self))
    self.btn_create.grid(row=2, column=4, padx=(10,0), pady=(10,0), sticky=E)
    self.btn_close = tk.Button(self.master, width=14, height=1, text='Close Program', command=lambda: webpage_gen_func.ask_quit(self))
    self.btn_close.grid(row=2, column=5, padx=(0,14), pady=(10,0), sticky=E)

    # user text field
    self.txt_add = tk.Entry(self.master, width=57, text='')
    self.txt_add.grid(row=1, column=1, rowspan=1, columnspan=6, padx=(14,40), pady=(38,0), sticky=N+E+W)


if __name__ == "__main__":
    pass
    
