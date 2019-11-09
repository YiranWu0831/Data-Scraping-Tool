# project: Data scraping Interface Design
# Author: Zihe Han
# Date: Semester 2, 2019

import time
from tkinter import *
from ForumPage import *
from SearchPage import *
from ThreadPage import *
from Soup import *

class HomePage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry("800x500+300+220")
        self.root.config(bg="lightblue")
        self.timestamp = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # Frame
        self.page.config(bg="lightblue")
        self.page.pack()
        Label(self.page, text='Welcome to Data Scraping program', font=('Arial', 25, 'bold'), fg='purple',
              bg="lightblue").pack(side='top')
        Label(self.page, bg="lightblue", height=1).pack()

        Label(self.page, bg="lightblue", width=35, height=2).pack()

        # scrape button
        self.timestamp.set(time.asctime(time.localtime(time.time())))
        Label(self.page, textvariable=self.timestamp, font=('Arial', 10), fg='purple', bg="lightblue").pack()
        Button(self.page, text='Scrape', font=('Arial', 12), command=self.clickCheck, width=22, height=2).pack()
        Label(self.page, bg="lightblue", width=35, height=2).pack()

        self.frame = Frame(self.page)
        self.frame.config(bg="lightblue")
        self.frame.pack()

        # search button
        Label(self.frame, text='Go to search page =>', bg="lightblue").grid(row=1, stick=W, padx=15, pady=20)
        Button(self.frame, text='Search', font=('Arial', 12), command=self.navSearchPage, width=25, height=2).grid(
            row=1, column=1, stick=E)
        # forum summary button
        Label(self.frame, text='Go to forum page =>', bg="lightblue").grid(row=2, stick=W, padx=15, pady=20)
        Button(self.frame, text='Forum Summary', font=('Arial', 12), command=self.navForumPage, width=25,
               height=2).grid(row=2, column=1, stick=E)
        # thread summary button
        Label(self.frame, text='Go to thread page =>', bg="lightblue").grid(row=3, stick=W, padx=15, pady=20)
        Button(self.frame, text='Thread Summary', font=('Arial', 12), command=self.navThreadPage, width=25,
               height=2).grid(row=3, column=1, stick=E)
        Label(self.page, bg="lightblue", width=35, height=1).pack()
        Label(self.page, text='The website to scrape is “Let’s Play!” Subforums of the Games forums',
              font=('Arial', 10, 'italic'), fg='purple', bg="lightblue").pack()
        self.canvas = Canvas(self.page, bg='white', height=75, width=800)
        self.image = PhotoImage(file="timg.gif")
        image = self.canvas.create_image(400, 0, anchor='n', image=self.image)
        self.canvas.pack()

    def navSearchPage(self):
        self.page.destroy()
        SearchPage(self.root)

    def navForumPage(self):
        self.page.destroy()
        ForumPage(self.root)

    def navThreadPage(self):
        self.page.destroy()
        ThreadPage(self.root)

    def clickCheck(self):
        localtime = time.asctime(time.localtime(time.time()))
        self.timestamp.set('Last scraping time: ' + localtime)



