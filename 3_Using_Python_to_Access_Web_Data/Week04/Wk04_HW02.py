# Week 04 Assignment 02
# Adam Britt
# 12/08/2018
#
# Problem Definition:
#
# Scraping Numbers from HTML using BeautifulSoup In this assignment you will
# write a Python program similar to http://www.py4e.com/code3/urllink2.py. The
# program will use urllib to read the HTML from the data files below, and parse
#  the data, extracting numbers and compute the sum of the numbers in the file.
#
# We provide two files for this assignment. One is a sample file where we give
# you the sum for your testing and the other is the actual data you need to
# process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_105082.html (Sum end
# with 85)
#
# You are to find all the <span> tags in the file and pull out the numbers from
# the tag and sum the numbers.
# Look at the sample code provided (http://www.py4e.com/code3/urllink2.py). It
# shows how to find all of a certain kind of tag, loop through the tags and
# extract the various aspects of the tags.
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
