# project: Data scraping Interface Design
# Author: Zihe Han & Yiran Wu
# Date: Semester 2, 2019

from tkinter import *
import HomePage
import tkinter.messagebox
import tkinter.ttk as ttk
from TitleDialog import *
from PostDialog import *
from CreatorDialog import *

class ThreadPage(object):
    def __init__(self, master=None):
        self.root = master
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # Frame
        self.page.pack()
        Label(self.page, text='Thread  Summary', font=('Arial', 25, 'bold'), fg='purple').pack(side='top')
        Label(self.page, text='Here we can see thread information for ‘Let’s Play’ Game Forum', font=('Arial', 12)).pack()
        global entry1
        entry1 = StringVar
        global entry2
        entry2 = StringVar
        # filter frame
        self.frame_1 = Frame(self.page)
        self.frame_1.pack()
        Label(self.frame_1, text='Filter By', font=('Arial', 15), fg='purple').grid(row=1, column=0, padx=5, pady=10)
        Label(self.frame_1, text='Date of last post from: ', bg='pink', font=('Arial', 12)).grid(row=1, column=1, padx=5, pady=10)
        Entry(self.frame_1, textvariable=entry1,show=None, font=('Arial', 12)).grid(row=1, column=2, padx=5, pady=10)
        Label(self.frame_1, text='To : ', bg='pink', font=('Arial', 12)).grid(row=1, column=3, padx=5, pady=10)
        Entry(self.frame_1, textvariable=entry2,show=None, font=('Arial', 12)).grid(row=1, column=4, padx=5, pady=10)
        Button(self.frame_1, text='Filter', font=('Arial', 15), width=10).grid(row=1, column=5, padx=5, pady=10)
        Label(self.frame_1).grid(row=2, column=0, padx=5, pady=10)

        # Summary table
        Label(self.page, text='Thread Table', font=('Arial', 15), fg='purple').pack()
        self.frame_2 = Frame(self.page)
        self.frame_2.pack()
        Label(self.frame_2, text='Noting: you can click on links in the following columns for more details:  '
                                 'Title of thread,  Number of accounts,  Posts/person,  and Creator', fg='brown', font=('Arial', 12)).pack()
        columns = ("title", "date", "posts", "accounts", "posts/person", "creator")
        table = ttk.Treeview(self.frame_2, show="headings", columns=columns)
        table.pack()
        # set table
        table.column('title', width=160, anchor='center')
        table.column('date', width=120, anchor='center')
        table.column('posts', width=120, anchor='center')
        table.column('accounts', width=120, anchor='center')
        table.column('posts/person', width=120, anchor='center')
        table.column('creator', width=100, anchor='center')

        table.heading('title', text='Title of thread')
        table.heading('date', text='Date of last post')
        table.heading('posts', text='Number of posts')
        table.heading('accounts', text='Number of accounts')
        table.heading('posts/person', text='Posts/person')
        table.heading('creator', text='Creator')

        table.insert('', 0, values=(Soup.list_thread_title[0], Soup.list_lastpost[0], Soup.list_post_number[0], '55',
                                    int(int(Soup.list_post_number[0])/55) , Soup.list_creator_name[0]))

        def filter(self):
            date_lastpost = entry1.get()
            index1 = Soup.list_creator_name.index(date_lastpost) if (date_lastpost in Soup.list_creator_name) else -1
            print(index1)
            date_lastpost = entry2.get()
            index2 = Soup.list_lastpost.index(date_lastpost) if (date_lastpost in Soup.list_lastpost) else -1
            columns = ("title", "date", "posts", "accounts", "posts/person", "creator")
            table = ttk.Treeview(self.frame_2, show="headings", columns=columns, height=5)
            table.pack()
            # set table
            table.column('title', width=240, anchor='center')
            table.column('date', width=120, anchor='center')
            table.column('posts', width=120, anchor='center')
            table.column('accounts', width=120, anchor='center')
            table.column('posts/person', width=120, anchor='center')
            table.column('creator', width=100, anchor='center')

            table.heading('title', text='Title of thread')
            table.heading('date', text='Date of first post')
            table.heading('posts', text='Number of posts')
            table.heading('accounts', text='Number of accounts')
            table.heading('posts/person', text='Posts/person')
            table.heading('creator', text='Creator')
            if index1 == -1 & index2 == -1:
                table.insert('', 0, values=("No matching result"))
                table.insert('', 1, )
                table.insert('', 2, )
                table.insert('', 3, )
                table.insert('', 4, )
            elif index1 != -1:
                table.insert('', 0, values=(
                    Soup.list_thread_title[index1], Soup.list_lastpost[index1], Soup.list_post_number[index1], '3',
                    int(Soup.list_post_number[index1]) / 3, Soup.list_creator_name[index1]))

        def openDialog(event):
            column = table.identify_column(event.x)
            row = table.identify_row(event.y)
            cn = str(column).replace('#', '')
            rn = str(row).replace('I00', '')
            if rn == '1' and cn == '1':
                TitleDialog.createDialog(self.root)
            elif rn == '1' and (cn == '4' or cn == '5'):
                PostDialog.createDialog(self.root)
            elif rn == '1' and cn == '6':
                CreatorDialog.createDialog(self.root)
            else:
                tkinter.messagebox.showinfo(title='Notice', message='Sorry! No more information.')

        table.bind('<Button-1>', openDialog)

        self.frame_3 = Frame(self.page)
        self.frame_3.pack()
        Label(self.frame_3).grid(row=0, column=0, padx=5, pady=10)
        Label(self.frame_3, text='Back to menu =>').grid(row=1, column=0, padx=5, pady=10)
        Button(self.frame_3, text='Back to Menu', font=('Arial', 12), width=12, height=2,
               command=self.returnHomePage).grid(row=1, column=1, padx=5, pady=10)

    def returnHomePage(self):
        self.page.pack_forget()
        HomePage.HomePage(self.root)
