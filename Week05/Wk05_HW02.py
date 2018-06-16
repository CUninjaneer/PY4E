# Week 05 Assignment 02
# Adam Britt
# 6/16/2018
#
# 3.2
#
# Write a program to prompt the user for hours and rate per hour using input to
# compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times
# the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate
# of 10.50 per hour to test the program (the pay should be 498.75). You should
# use input to read a string and float() to convert the string to a number. Do
# not worry about error checking the user input - assume the user types numbers
# properly.
#
# Desired Output = 498.75
#
################################################################################

# Gather user inputs
hrs = input("Enter hours worked: ")
h = float(hrs)
rate = input("Enter hourly pay rate in Dollars per Hour: ")
r = float(rate)

# Determine hours eligible for overtime pay
ot_threshhold = 40
if h > ot_threshhold :
    st = ot_threshhold
    ot = h - st
else :
    st = h
    ot = 0

# Calculate and report pay due to user
wage = (st * r) + (ot * r * 1.5)
print(wage)
