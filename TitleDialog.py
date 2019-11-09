# project: Data scraping Interface Design
# Author: Zihe Han
# Date: Semester 2, 2019


import tkinter as tk
import Soup
from tkinter import *
import webbrowser

class TitleDialog(object):
    def __init__(self):
        self = tk.Tk()
        self.createDialog()
        self.callback()

    def createDialog(self):
        window = tk.Toplevel(self)
        window.title('Title dialog box')
        window.geometry('300x230+400+400')
        page = tk.Frame(window)  # Frame
        page.pack()
        tk.Label(page, text=Soup.list_thread_title[0], font=('Arial', 25, 'bold'), fg='brown').pack(side='top')
        message = "Link: " + Soup.list_thread_link[0]
        msg = tk.Message(page, text=message)
        msg.config(bg='lightyellow', font=('Arial', 17, 'italic'), aspect=220)
        msg.pack()

        webbrowser.open_new(Soup.list_thread_link[0])

        #button1 = tk.LEFT(self)
        #link = Label(button1, text="Open", fg="blue", cursor="hand2")
        #link.pack()
        #link.bind("<Button-1>")
