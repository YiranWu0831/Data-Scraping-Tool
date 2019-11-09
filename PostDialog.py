# project: Data scraping Interface Design
# Author: Zihe Han
# Date: Semester 2, 2019

import tkinter as tk
import tkinter.ttk as ttk
class PostDialog(object):
    def __init__(self):
        self = tk.Tk()
        self.createDialog()

    def createDialog(self):
        window = tk.Toplevel(self)
        window.title('Posts dialog box')
        window.geometry('500x280+460+350')
        page = tk.Frame(window)  # Frame
        page.pack()
        tk.Label(page, text='Table of posters', font=('Arial', 25, 'bold'), fg='brown').pack(side='top')

        # poster table
        frame = tk.Frame(page)
        frame.pack()
        tk.Label(frame, text='Total posts: 5', font=('Arial', 15)).grid(row=0, column=0, padx=5, pady=15)
        frame_2 = tk.Frame(page)
        frame_2.pack()
        columns = ("posters", "posts")
        table = ttk.Treeview(frame_2, show="headings", columns=columns, height=3)
        table.pack()
        # set table
        table.column('posters', width=100, anchor='center')
        table.column('posts', width=100, anchor='center')

        table.heading('posters', text='Poster')
        table.heading('posts', text='Number of posts')

        table.insert('', 0, values=('David *', 3))
        table.insert('', 1, values=('Jane', 1))
        table.insert('', 2, values=('Rachel', 1))

        tk.Label(frame_2).pack()
        tk.Label(page, text='Noting: * = Top', font=('Arial', 12), fg='brown').pack(side='bottom')

