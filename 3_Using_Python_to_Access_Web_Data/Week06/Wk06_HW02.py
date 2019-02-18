# Course 03
# Week 06 Assignment 02
# Adam Britt
# 2/17/2019
#
# Problem Definition:
#
#   Write a program to prompt for a URL and read the JSON data from that URL
#   using urllib.  Then parse and extract the comment counts from the XML data,
#   and compute the sum of the numbers in the file.
#
# Data Format and Approach:
#
#   The data consistsof a number of names and comment counts as follows:
#
#       {
#         comments: [
#           {
#             name: "Matthias"
#             count: 97
#           },
#           {
#             name: "Geomer"
#             count: 97
#           }
#           ...
#         ]
#       }
#
#   Look through the root dictionary for the "comment" key.  The value for that
#   key is a list of dictionaries, look in each dictionary of the list for a
#   "count" key, and sum the values of those keys.
#
#   To make the code a little simpler, you can use an XPath selector string
#   to look through the entire tree of XML for and tag named "count" with the
#   following line of code:
#       counts = tree.findall('.//count')
#   Take a look at the Python ElementTree documentation and look for the
#   supported XPath syntax for details
#
#
# Sample Execution:
#   $ python3 solution.py
#   Enter location: http://py4e-data.dr-chuck.net/comments_42.json
#   Retrieving http://py4e-data.dr-chuck.net/comments_42.json
#   Retrieved 2733 characters
#   Count: 50
#   Sum: 2553
#
#
################################################################################
import sys
import urllib.request, urllib.parse, urllib.error
import json

# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
# url = 'http://py4e-data.dr-chuck.net/comments_105085.json'
url = input('Enter URL: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters.')

info = json.loads(data)

total = 0

for item in info["comments"]:
    total = total + int(item["count"])

print('Sum :', total)

# sys.exit()
