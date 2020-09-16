from functools import reduce


def binary(num):
    num = int(num)
    rem = []
    while num:
        rem.append(num % 2)
        num //= 2

    rem = rem[::-1]
    return reduce(lambda x, y: x*10+y, rem)


def decimal(num):
    num = list(num)
    lst = []
    for i in range(len(num)):
        lst.append(int(num[i])*(2**i))
    return sum((lst))


print("\tBinary Convertor")
print("1.Decimal to Binary\n2. Binary to Decimal")
ch = int(input("Enter your choice : "))
num = input("Enter the number : ")
if ch == 1:
    result = binary(num)
elif ch == 2:
    result = decimal(num)
else:
    print("Wrong choice...!!")
    exit()

print(result)
