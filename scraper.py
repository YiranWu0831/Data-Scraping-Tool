
# scraper for posts on the Something Awful forums

# modified from https://gist.github.com/Ell/6679837



#!/usr/local/bin/python2



import StringIO



import requests

import grequests

import redis

from lxml import etree

from lxml.etree import tostring

from itertools import chain



posts_text = []



class AwfulScraper(object):

    def __init__(self, username, password, thread_url):

        self.username = username

        self.password = password

        self.thread_url = thread_url



        self.session = requests.Session()

        self.login()



    def login(self):

        data = {

            'action': 'login',

            'username': self.username,

            'password': self.password,

            'next': '/'

        }



        self.session.post('https://forums.somethingawful.com/account.php', data=data)



    def scrape_page(self, response, *args, **kwargs):

        print ("Scraping " + response.url)

        html = response.text

        doc = etree.parse(StringIO.StringIO(html), etree.HTMLParser())

        posts = doc.xpath('//td[@class="postbody"]')



        for node in posts:

            parts = ([node.text] + list(chain(*([c.text, tostring(c, with_tail=False), c.tail] for c in node.getchildren()))) + [node.tail])

            node_text = ''.join(filter(None, parts))

            posts_text.append(node_text)



    def scrape_thread(self, start=1, pages_to_get=1):

        # pages_to_get is the number of pages of the thread to scrape -- if it's set to -1

        # or a number bigger than the actual number of pages in the thread being scraped 

        # then the scraper will just scrape the entire thread

        html = self.session.get(self.thread_url).text

        parser = etree.HTMLParser()

        doc = etree.parse(StringIO.StringIO(html), parser)

        page_count = doc.xpath('//a[contains(@title, "Last")]/text()')[0].split(' ')[0]



        num_pages_to_get = pages_to_get

        if (num_pages_to_get < 0) or (num_pages_to_get > page_count):

            num_pages_to_get = page_count

        

        pages = [self.thread_url+'&pagenumber='+str(page_num) for page_num in range(start, int(num_pages_to_get + 1))]

        reqs = [grequests.get(url, callback=self.scrape_page, session=self.session) for url in pages]

        resp = grequests.map(reqs, size=1)





if __name__ == '__main__':

    username = ''

    password = ''

    thread_url = 'https://forums.somethingawful.com/showthread.php?threadid=3846968'

    a = AwfulScraper(username, password, thread_url)

    a.scrape_thread(start=1, pages_to_get=1)



    posts_text = [p for p in posts_text if "adbot" not in p]

    for p in posts_text:

        print(p)

        print('NEXT POST NEXT POST NEXT POST')



    print ("Scraping Completed.")
