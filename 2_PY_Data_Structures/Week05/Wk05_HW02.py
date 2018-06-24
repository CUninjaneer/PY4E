# Week 05 Assignment 02
# Adam Britt
# 6/24/2018
#
# 9.4
#
# Problem Definition:
#
# Write a program to read through the mbox-short.txt and figure out who has the
# sent the greatest number of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.
#
#
# Desired Output:
#
#   cwen@iupui.edu 5
#
#
################################################################################

fname = input("Enter file name: ")
# avoid tracebacks from bad filenames
try:
    fhand = open(fname)
except:
    print('ERROR: File', fname, 'cannot be opened.')
    quit()
# initialize any empty list to collect words

emails = list()
# parse inidividual lines
for line in fhand :
    # break lines into words for further parsing
    pieces = line.split()
    if pieces == [] or pieces[0] != 'From' : continue
    emails.append(pieces[1]) # collect email address in list

# build the dictionary with emails and their frequencies
counts = dict()
for email in emails :
    counts[email] = counts.get(email,0) + 1

# loop through dictionary to find the word with the max frequency
bigcount = None
bigemail = None
for email,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigemail = email
        bigcount = count

# print the results
print(bigemail, bigcount)
