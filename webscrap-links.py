# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
position = int(input('Enter position -'))
count = int(input('Enter count -'))
i = 0
while (i < count):
    name = list()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        name.append(tag.get('href', None))
    url=name[position-1]
    i = i + 1
name = re.findall('known_by_([A-Za-z]*)', url)
print(name[0])
