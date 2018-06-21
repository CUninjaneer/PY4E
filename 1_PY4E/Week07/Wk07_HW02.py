# Week 06 Assignment 02
# Adam Britt
# 6/20/2018
#
# Example 5.1 from PY4E Textbook
#
# Write a program that repeatedly prompts a user for integer numbers until the
# user enters 'done'. Once 'done' is entered, print out the largest and smallest
# of the numbers. If the user enters anything other than a valid number catch it
# with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.
#
# Desired Output:
#   Invalid input
#   Maximum is 10
#   Minimum is 2
#
################################################################################

smallest = None
largest = None
while True :
    sval = input('Enter an integer: ')
    if sval == 'done' :
        break
    if sval == 'Done' :
        break
    try :
        ival = int(sval)
    except :
        print('Invalid input')
    if smallest is None :
        smallest = ival
    elif ival < smallest :
        smallest = ival
    if largest is None :
        largest = ival
    elif ival > largest :
        largest = ival
print('Maximum is', largest)
print('Minimum is', smallest)