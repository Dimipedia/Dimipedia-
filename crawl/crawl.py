#-*- coding: utf-8 -*-

"""
crawl.py

Created by Mase Kim on July 19, 2016.
Copyright (c) 2016 Mase Kim. All rights reserved.

"""

import urllib2, requests
from bs4 import BeautifulSoup

url = urllib2.urlopen('http://dimipedia.net/w/index.php?title=%ED%8A%B9%EC%88%98:%EB%AA%A8%EB%93%A0%EB%AC%B8%EC%84%9C&from=&to=&namespace=1')
soup = BeautifulSoup(url, "html.parser")
soup.prettify()
print soup
mydatas = soup.find_all('ul', {'class':"mw-allpages-chunk"})
print mydatas