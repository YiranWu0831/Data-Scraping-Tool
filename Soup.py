# project: Data scraping Interface Design
# Author: Yiran Wu
# Date: Semester 2, 2019

import time
import requests
from bs4 import BeautifulSoup
start = time.clock()
response = requests.get('https://forums.somethingawful.com/forumdisplay.php?forumid=191').text
#https://forums.somethingawful.com/forumdisplay.php?forumid=191&daysprune=30&perpage=30&posticon=0&sortorder=desc&sortfield=lastpost&pagenumber=93
t = 2
for t in range(2,93):
    response = requests.get('https://forums.somethingawful.com/forumdisplay.php?forumid=191&daysprune=30&perpage=30&posticon=0&sortorder=desc&sortfield=lastpost&pagenumber='+str(t)).text+response

    t = t+1
#response.encoding = 'utf-8'
soup = BeautifulSoup(response, 'html.parser')



#response = requests.get('https://forums.somethingawful.com/forumdisplay.php?forumid=191')
#https://forums.somethingawful.com/forumdisplay.php?forumid=191&daysprune=30&perpage=30&posticon=0&sortorder=desc&sortfield=lastpost&pagenumber=93

#response.encoding = 'utf-8'
#soup = BeautifulSoup(response.text, 'html.parser')
# news = soup.find_all('div', {"class": "info"})
thread = soup.find_all('tr', {"class": "thread"})


f = open('C:/Users/wuyir/Desktop/c.txt', 'w+')

# get the title and link of each thread

news = soup.find_all('div', {"class": "info"})


def thread_function():
    global thread_count
    thread_count = 0
    global list_thread_link
    list_thread_link = []
    global list_thread_title
    list_thread_title = []
    for t in news:
        thread_count = thread_count + 1
        print ('Title: ', ''.join(t.find('a').text))
        f.write('Title: '+''.join(t.find('a').text)+'#')
        f.write('Link: ''https://forums.somethingawful.com/'+''.join(t.find('a')['href']+'#'))
        # .split can be used for cutting down strings
        print ('Link: ''https://forums.somethingawful.com/'+''.join(t.find('a')['href']))  # .join is used to get rid of u'

        #  list for capturing the text in posts
        list_thread_title.append(''.join(t.find('a').text))
        list_thread_link.append('https://forums.somethingawful.com/' + t.find('a')['href'])


thread_function()


def thread_count_function():
    return thread_count


# thread_count_function()

# get the number of posts in each thread

post = soup.findAll('td', {"class": "replies"})


def post_function():
    global reply_num_list_count
    reply_num_list_count = 0
    global sum_post
    sum_post = 0
    global list_post_number
    list_post_number = []
    for p in post:
        post_num = post[reply_num_list_count].get_text()
        list_post_number.append(post_num)
        if post_num != '-':
            sum_post = sum_post + int(post_num)
        reply_num_list_count = reply_num_list_count + 1
        print (post_num)
        f.write(post_num + "#")


post_function()


def sum_post_function():
    print(sum_post)
    return sum_post


sum_post_function()

# get the creator of the thread

creator = soup.findAll('td', {"class": "author"})


def creator_function():
    global creator_list_count
    creator_list_count = 0
    global list_creator_name
    list_creator_name = []
    for c in creator:
        creator_name = creator[creator_list_count].get_text()
        list_creator_name.append(creator_name)
        creator_list_count = creator_list_count + 1
        print (creator_name)
        f.write(creator_name + "#")


creator_function()
# get the time of last post

lastpost = soup.findAll('div', {"class": "date"})


def lastpost_function():
    global lastpost_count
    lastpost_count = 0
    global list_lastpost
    list_lastpost = []
    for l in lastpost:
        lastpost_time = lastpost[lastpost_count].get_text()
        list_lastpost.append(lastpost_time)
        lastpost_count = lastpost_count + 1
        print (lastpost_time)
        f.write(lastpost_time + "#")


lastpost_function()

elapsed = (time.clock() - start)
print("Time used:",elapsed)


def poster_number():
    set1 = set(list_creator_name)
    print(len(set1))

poster_number()
