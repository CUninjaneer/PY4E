# Week 02 Assignment 02
# Adam Britt
# 6/28/2018
#
# Problem Definition:
#
# Finding a Number in a Haystack
#
# In this assignment you will read through and parse a file with text and
# numbers. You will extract all the numbers in the file and compute the sum
# of the numbers.
#
# Data Files
#
# We provide two files for this assignment. One is a sample file where we
# give you the sum for your testing and the other is the actual data you need
# to process for the assignment.
#
#   •   Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt  (There
#       are 90 values with a sum=445833)
#   •   Actual data: http://py4e-data.dr-chuck.net/regex_sum_105080.txt 
#       (There are 100 values and the sum ends with 162)
#
# Data Format
#
# The file contains much of the text from the introduction of the textbook
# except that random numbers are inserted throughout the text.
# The numbers can appear anywhere in the line. There can be any number of
# numbers in each line (including none).
#
# Handling the Data
#
# The basic outline of this problem is to read the file, look for integers
# using the re.findall(), looking for a regular expression of '[0-9]+' and
# then converting the extracted strings to integers and summing up the
# integers.
#
# Desired Output:
#
#   %a number ending in 162%
#
#
################################################################################

#fname = 'regex_sum_42.txt'
#fname = 'regex_sum_105080.txt'
#fhand = open(fname)

#import re

#numbers = re.findall('[0-9]+', open('regex_sum_105080.txt').read())

# # initialize any empty list to collect numbers
# numbers = list()
# # parse inidividual lines
# for line in fhand :
#     x = re.findall('[0-9]+', line)
#     if len(x) < 1 : continue
#     for i in range(len(x)) :
#         numbers.append(int(x[i])) # collect results in list

#total = sum([int(i) for i in numbers])

#sum = 0
#for num in numbers : sum = sum + int(num)

#print('There are', len(numbers), 'values with a sum of', total)

import re
print( sum( [ int(i) for i in re.findall('[0-9]+', open('regex_sum_105080.txt').read()) ] ) )
