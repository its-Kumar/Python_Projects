from math import pi
n = int(input("Enter a number : "))
if n > 15 or n < 0:
    print("Please Enter the value between 0 to 15 .!!")
else:
    p = str(pi)
    print("PI upto {} decimal place = {}".format(n, p[:n+2]))
