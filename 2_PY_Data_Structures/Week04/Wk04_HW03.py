# Week 03 Assignment 02
# Adam Britt
# 6/22/2018
#
# 8.5
#
# Problem Definition:
#
# Open the file mbox-short.txt and read it line by line. When you find a line
# that starts with 'From ' like the following line:
#
#   From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# You will parse the From line using split() and print out the second word in
# the line (i.e. the entire address of the person who sent the message). Then
# print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
#
#
# Desired Output:
#
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
# rjlowe@iupui.edu
# zqian@umich.edu
# rjlowe@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# gsilver@umich.edu
# gsilver@umich.edu
# zqian@umich.edu
# gsilver@umich.edu
# wagnermr@iupui.edu
# zqian@umich.edu
# antranig@caret.cam.ac.uk
# gopal.ramasammycook@gmail.com
# david.horwitz@uct.ac.za
# david.horwitz@uct.ac.za
# david.horwitz@uct.ac.za
# david.horwitz@uct.ac.za
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# louis@media.berkeley.edu
# ray@media.berkeley.edu
# cwen@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word
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
lst = list()
# parse inidividual lines
for line in fhand :
    # break lines into words for further parsing
    pieces = line.split()
    
    if pieces == [] or pieces[0] != 'From' : continue
    lst.append(pieces[1]) # collect email address in list
    print(pieces[1])
print('There were', len(lst), 'lines in the file with From as the first word')
