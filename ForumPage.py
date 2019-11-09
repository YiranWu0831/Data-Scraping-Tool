# project: Data scraping Interface Design
# Author: Zihe Han
# Date: Semester 2, 2019


from tkinter import *
from ThreadPage import *
import HomePage
import Soup
class ForumPage(object):
    def __init__(self, master=None):
        self.root = master
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # Frame
        self.page.pack()
        Label(self.page, text='Forum  Summary', font=('Arial', 25, 'bold'), fg='purple').pack(side='top')
        Label(self.page, text='Here we can see an overview of forum information for ‘Let’s Play’ Game Forum', fg='brown', font=('Arial', 12, 'italic')).pack()

        # page information
        self.frame = Frame(self.page)
        self.frame.pack()

        Label(self.frame, text='* Number of threads:', bg='lightyellow', font=('Arial', 12), width=25, height=2).grid(row=1, column=1,  pady=20)
        Label(self.frame, text= Soup.thread_count_function(), bg='lightyellow', font=('Arial', 12), width=25, height=2).grid(row=1, column=2,  pady=20)
        Label(self.frame, text='* Number of posters:', bg='lightyellow', font=('Arial', 12), width=25, height=2).grid(row=2, column=1,  pady=20)
        Label(self.frame, text='3948', bg='lightyellow', font=('Arial', 12), width=25, height=2).grid(row=2, column=2,  pady=20)
        Label(self.frame, text='* Number of posts:', bg='lightyellow', font=('Arial', 12), width=25, height=2).grid(row=3, column=1,  pady=20)
        Label(self.frame, text= Soup.sum_post_function(), bg='lightyellow', font=('Arial', 12), width=25, height=2).grid(row=3, column=2,  pady=20)

        # detail button
        Label(self.frame).grid(row=4, column=0, padx=5, pady=10)
        Label(self.frame, text='For more details =>').grid(row=5, column=0, padx=5, pady=20)
        Button(self.frame, text='Thread Summary', font=('Arial', 12), command=self.navThreadPage, width=20, height=2).grid(row=5, column=1, padx=5, pady=20)

        Label(self.frame, text='Back to menu =>').grid(row=5, column=2, padx=5, pady=20)
        Button(self.frame, text='Go to Menu', font=('Arial', 12), width=20, height=2,
               command=self.returnHomePage).grid(row=5, column=3, padx=5, pady=10)
        self.canvas = Canvas(self.page, bg='lightblue', height=75, width=320)
        self.image = PhotoImage(file="timg.gif")
        image = self.canvas.create_image(160, 0, anchor='n', image=self.image)
        self.canvas.pack()

    def navThreadPage(self):
        self.page.destroy()
        ThreadPage(self.root)
    def returnHomePage(self):
        self.page.destroy()
        HomePage.HomePage(self.root)