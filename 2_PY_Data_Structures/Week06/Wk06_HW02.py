# Week 06 Assignment 02
# Adam Britt
# 6/27/2018
#
# 10.2
#
# Problem Definition:
#
# Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
#
#   From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.
#
#
# Desired Output:
#
#   04 3
#   06 1
#   07 1
#   09 2
#   10 3
#   11 6
#   14 1
#   15 2
#   16 4
#   17 2
#   18 1
#   19 1
#
#
################################################################################

fname = input("Enter file name: ")
if len(fname) < 1: fname = 'mbox-short.txt'
# avoid tracebacks from bad filenames
try:
    fhand = open(fname)
except:
    print('ERROR: File', fname, 'cannot be opened.')
    quit()
# initialize any empty list to collect words

times = list()
# parse inidividual lines
for line in fhand :
    # break lines into words for further parsing
    pieces = line.split()
    if pieces == [] or pieces[0] != 'From' : continue
    hms = pieces[5].split(':')
    hour = hms[0]
    times.append(hour) # collect times in list

# build the dictionary with emails and their frequencies
counts = dict()
for time in times :
    counts[time] = counts.get(time,0) + 1

for k,v in sorted(counts.items()): print(k,v)
