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


import os
import webbrowser as wb
from tkinter import *
from tkinter import messagebox

import webpage_gen_gui
import webpage_gen_main


# this centers the gui window
def center_window(self, w, h):  # Pass in the tkinter frame (master) reference and the w and h
    # Get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # Calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# we use this function to ask user before closing the program
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


def onClear(self):
    # Clear the text in these textboxes
    self.txt_add.delete(0,END)



# this function creates the webpage with the users input
def create_file(self):
    hFile = open("index.html","w")
    usertext = self.txt_add.get()

    if usertext != '':
        hFile.write("""
        <html>
            <body>
                <h1>
                    {}
                </h1>
            <body>
        </html>
        """.format(usertext))
        hFile.close()
        wb.open_new_tab("index.html")
    else:
        messagebox.showinfo(title="Error", message="Please insert text into field")



if __name__ == "__main__":
    pass
