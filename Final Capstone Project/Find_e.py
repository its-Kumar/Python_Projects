from math import e

n = int(input("Enter a number : "))
if n > 15 or n < 0:
    print("Please Enter the value between 0 to 15 .!!")
else:
    e_val = str(e)
    print("e upto {} decimal place = {}".format(n, e_val[:n+2]))
