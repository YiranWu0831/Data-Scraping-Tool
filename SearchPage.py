# project: Data scraping Interface Design
# Author: Zihe Han & Yiran Wu
# Date: Semester 2, 2019

from tkinter import *
import tkinter.messagebox
import HomePage
import tkinter.ttk as ttk
from TitleDialog import *
from PostDialog import *
from CreatorDialog import *
import Soup
class SearchPage(object):
    def __init__(self, master=None):
        self.root = master
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # Frame
        self.page.pack()
        Label(self.page, text='Search Page', font=('Arial', 25, 'bold'), fg='purple').pack(side='top')
        # search frame
        self.frame_1=Frame(self.page)
        self.frame_1.pack()
        global v1, v2, v3
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        Label(self.frame_1, text='Search By', font=('Arial', 15), fg='purple').grid(row=1, column=0, padx=5, pady=15)
        Label(self.frame_1, text="Creator's username: ", bg='pink', font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=15)
        Entry1 = Entry(self.frame_1, textvariable=v1, show=None, font=('Arial', 10)).grid(row=2, column=1, padx=5, pady=15)


        Label(self.frame_1, text='Date of the last post : ', bg='pink', font=('Arial', 12)).grid(row=2, column=2, padx=5, pady=15)
        Entry2 = Entry(self.frame_1, textvariable=v2, show=None, font=('Arial', 10)).grid(row=2, column=3, padx=5, pady=15)


        Label(self.frame_1, text='Title of thread : ', bg='pink', font=('Arial', 12)).grid(row=2, column=4, padx=5, pady=15)
        Entry3 = Entry(self.frame_1, textvariable=v3, show=None, font=('Arial', 10)).grid(row=2, column=5, padx=5, pady=15)



        # search button
        Button(self.frame_1, text='Search', font=('Arial', 15), width=10).grid(row=3, column=5, padx=5, pady=15)
        # click button: response
        # Search table
        Label(self.page, text='Result Table', font=('Arial', 15), fg='purple').pack()
        self.frame_2 = Frame(self.page)
        self.frame_2.pack()
        Label(self.frame_2, text='Noting: you can click on links in the following columns for more details:  '
                                 'Title of thread,  Number of accounts,  Posts/person,  and Creator', fg='brown',
              font=('Arial', 12)).pack()

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
        table.heading('date', text='Date of last post')
        table.heading('posts', text='Number of posts')
        table.heading('accounts', text='Number of accounts')
        table.heading('posts/person', text='Posts/person')
        table.heading('creator', text='Creator')

        table.insert('', 0, values=(Soup.list_thread_title[1], Soup.list_lastpost[1], Soup.list_post_number[1], '56',
                                    int(int(Soup.list_post_number[1])/56), Soup.list_creator_name[1]))
        #table.insert('', 1, values=(Soup.list_thread_title[1], Soup.list_lastpost[1], Soup.list_post_number[1], '3',
         #                           int(Soup.list_post_number[1]) / 3, Soup.list_creator_name[1]))
        #table.insert('', 2, values=(Soup.list_thread_title[2], Soup.list_lastpost[2], Soup.list_post_number[2], '3',
         #                           int(Soup.list_post_number[2]) / 3, Soup.list_creator_name[2]))
        #table.insert('', 3, values=(Soup.list_thread_title[3], Soup.list_lastpost[3], Soup.list_post_number[3], '3',
          #                       int(Soup.list_post_number[3]) / 3, Soup.list_creator_name[3]))
        #table.insert('', 4, values=(Soup.list_thread_title[4], Soup.list_lastpost[4], Soup.list_post_number[4], '3',
         #                           int(Soup.list_post_number[4]) / 3, Soup.list_creator_name[4]))


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
        Label(self.frame_3).grid(row=0, column=0, padx=5, pady=15)
        Label(self.frame_3, text='Back to menu =>').grid(row=1, column=0, padx=5, pady=20)
        Button(self.frame_3, text='Back to Menu', font=('Arial', 12), width=12, height=2,
               command=self.returnHomePage).grid(row=1, column=1, padx=5, pady=15)

    def search(self):
        creator_name = v1.get()
        index1 = Soup.list_creator_name.index(creator_name) if (creator_name in Soup.list_creator_name) else -1
        print(index1)
        date_lastpost = v2.get()
        index2 = Soup.list_lastpost.index(date_lastpost) if (date_lastpost in Soup.list_lastpost) else -1
        title_name = v3.get()
        index3 = Soup.list_thread_title.index(title_name) if (title_name in Soup.list_thread_title) else -1
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
        if index1 == -1 & index2 == -1 & index3 == -1:
            table.insert('', 0, values=("No matching result"))
            table.insert('', 1, )
            table.insert('', 2, )
            table.insert('', 3, )
            table.insert('', 4, )
        elif index1 != -1:
            table.insert('', 0, values=(
                Soup.list_thread_title[index1], Soup.list_lastpost[index1], Soup.list_post_number[index1], '3',
                int(Soup.list_post_number[index1]) / 3, Soup.list_creator_name[index1]))
    def returnHomePage(self):
        self.page.destroy()
        HomePage.HomePage(self.root)

