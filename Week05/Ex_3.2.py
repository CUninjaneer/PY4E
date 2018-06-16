# Week 05 Assignment 02
# Adam Britt
# 6/16/2018
#
# 3.2
#
# Adding error checking to the assignment we just did.
#
################################################################################

# Gather user inputs
hrs = input("Enter hours worked: ")
rate = input("Enter hourly pay rate in Dollars per Hour: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("ERROR: Enter numeric values only.")
    quit()

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
print("Your pay will be", wage)
