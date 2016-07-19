#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

r = requests.get('http://dimipedia.net/w/index.php?title=특수%3A모든문서&from=&to=&namespace=1&hideredirects=1')
soup = BeautifulSoup(r.text, "html.parser")
print soup
for link in soup.find("ul", {"class" : "mw-allpages-chunk"}):
    href = link.get('href')
    title = link.string
    print "www.dimipedia.net" + href
    print title