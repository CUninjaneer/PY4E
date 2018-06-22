# Week 03 Assignment 02
# Adam Britt
# 6/22/2018
#
# 7.2
#
# Write a program that prompts for a file name, then opens that file and reads
# through the file, looking for lines of the form:
#
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output as shown
# below. Do not use the sum() function or a variable named sum in your
# solution.
# You can download the sample data at  http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.
#
#
# Desired Output:
#   Average spam confidence: 0.750718518519
#
#
################################################################################

# Use the file name mbox-short.txt as the file name
fname = input('Enter the file name: ')
# avoid tracebacks from bad filenames
try:
    fhand = open(fname)
except:
    print('ERROR: File', fname, 'cannot be opened.')
    quit()
# initialize variables
count = 0
total = 0
# find the numbers line by line
for line in fhand :
    # skip uninteresting lines
    if not line.startswith("X-DSPAM-Confidence:") : continue
    # increment counter when an interesting line is found
    count = count + 1
    # extract the confidence, convert to number, and add to total
    colpos = line.find(':')
    strconf = line[ colpos+1 : ].strip()
    numconf = float(strconf)
    total = total + numconf
# calculate and print average confidence
avgconf = total / count
print('Average spam confidence:', avgconf)
