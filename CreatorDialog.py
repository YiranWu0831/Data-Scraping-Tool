# project: Data scraping Interface Design
# Author: Zihe Han
# Date: Semester 2, 2019

import tkinter as tk

class CreatorDialog(object):
    def __init__(self):
        self = tk.Tk()
        self.createDialog()

    def createDialog(self):
        window = tk.Toplevel(self)
        window.title('Creator dialog box')
        window.geometry('600x350+460+300')
        page = tk.Frame(window)  # Frame
        page.pack()
        tk.Label(page, text='Creator information', font=('Arial', 25, 'bold'), fg='brown').pack(side='top')

        frame = tk.Frame(page)
        frame.pack()
        tk.Label(frame, text='* Username :', bg='pink', font=('Arial', 15), width=20, height=2).grid(row=1, column=0, padx=5, pady=10)
        tk.Label(frame, text='Artix', bg='lightyellow', font=('Arial', 15), width=20, height=2).grid(row=1, column=1, padx=5, pady=10)
        tk.Label(frame, text='* Gender:', bg='pink', font=('Arial', 15), width=20, height=2).grid(row=2, column=0, padx=5, pady=10)
        tk.Label(frame, text='Male', bg='lightyellow', font=('Arial', 15), width=20, height=2).grid(row=2, column=1, padx=5, pady=10)
        tk.Label(frame, text='* Number of posts:', bg='pink', font=('Arial', 15), width=20, height=2).grid(row=3, column=0, padx=5, pady=10)
        tk.Label(frame, text='36', bg='lightyellow', font=('Arial', 15), width=20, height=2).grid(row=3, column=1, padx=5, pady=10)
        tk.Label(frame, text='* Thread Title:', bg='pink', font=('Arial', 15), width=20, height=2).grid(row=4, column=0, padx=5,pady=10)

        message = "Let us play with League of Legends! I need a new group and there are three members here."
        msg = tk.Message(frame, text=message, aspect=220)
        msg.config(bg='yellow', font=('Arial', 14, 'italic'))
        msg.grid(row=4, column=1, padx=5, pady=10)
