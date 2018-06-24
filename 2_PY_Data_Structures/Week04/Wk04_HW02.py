# Week 03 Assignment 02
# Adam Britt
# 6/22/2018
#
# 8.4
#
# Problem Definition:
#
# Open the file romeo.txt and read it line by line. For each line, split the
# line into a list of words using the split() method. The program should build
# a list of words. For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program
# completes, sort and print the resulting words in alphabetical order.
#
#
# Desired Output:
#
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
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
lst = list()
# parse inidividual lines
for line in fhand :
    # break lines into words for further parsing
    pieces = line.split()
    for word in pieces :
        if word in lst : continue # ignore duplicate words
        lst.append(word)
# sort and print
lst.sort()
print(lst)
