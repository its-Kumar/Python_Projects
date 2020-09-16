def fibnacci(num):
    a, b = 0, 1
    while num:
        yield a
        a, b = b, a+b
        num -= 1


def fib_seq(num):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
        if num < a:
            break


n = int(input("Enter any number : "))
print(f"Fibnacci sequence upto {n} terms = ")
for t in fibnacci(n):
    print(t)

print(f"\nFibnacci sequence upto {n} = ")

for t in fib_seq(n):
    print(t)
