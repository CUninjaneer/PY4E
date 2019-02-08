# Week 04 Assignment 02
# Adam Britt
# 12/08/2018
#
# Problem Definition:
#
# 
#
#
################################################################################

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_105082.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
total = 0
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('class', tag.get('span', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    total = total + int(tag.contents[0])

print('Sum =', total)
