# Week 01 Assignment 02
# Adam Britt
# 6/21/2018
#
# 6.5
#
# Write code using find() and string slicing (see section 6.10) to extract the
# number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.
#
# Line below:
#   text = "X-DSPAM-Confidence:    0.8475";
#
# Desired Output:
#   0.8475
#
################################################################################

text = "X-DSPAM-Confidence:    0.8475";
colpos = text.find(':')
numstr = text[colpos+1 : ]
numstr2 = numstr.strip()
num = float(numstr)
print(num)
