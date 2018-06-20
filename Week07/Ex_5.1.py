# Week 07 Worked Example
# Adam Britt
# 6/20/2018
#
# Example 5.1 from PY4E Textbook
#
# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.
#
#
################################################################################

count = 0
total = 0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    if sval == 'Done' :
        break
    try :
        fval = float(sval)
    except :
        print('ERROR: Enter numerical values only')
        continue
    count = count + 1       #counter pattern
    total = total + fval    # accumulator pattern
print('Count =', count)
print('Total =', total)
print('Average = ', total/count)
