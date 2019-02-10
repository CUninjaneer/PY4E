# Week 04 Assignment 02
# Adam Britt
# 12/08/2018
#
# Problem Definition:
#
#   Write a program to prompt for a URL and read the XML data from that URL
#   using urllib.  Then parse and extract the comment counts from the XML data,
#   and compute the sum of the numbers in the file.
#
# Data Format and Approach:
#
#   The data consistsof a number of names and comment counts as follows:
#       <comment>
#           <name>Matthias</name>
#           <count>97</count>
#       </comment>
#
#   Look through all the <comment> tags, find the <count> values, and sum the
#   numbers.
#   To make the code a little simpler, you can use and XPath selector string
#   to look through the entire tree of XML for and tag named "count" with the
#   following line of code:
#       counts = tree.findall('.//count')
#   Take a look at the Python ElementTree documentation and look for the
#   supported XPath syntax for details
#
#
# Sample Execution:
#   $ python3 solution.py
#   Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
#   Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
#   Retrieved 4189 characters
#   Count: 50
#   Sum: 2...
#
#
################################################################################
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
#url = 'http://py4e-data.dr-chuck.net/comments_105084.xml'
url = input('Enter URL: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters.')

tree = ET.fromstring(data)
counts = tree.findall(".//count")
print('Count:', len(counts))

total = 0

for count in counts:
     total = total + int(count.text)

print('Sum :', total)
