def find_prime(num):
    lst = []
    for i in range(2, num):
        if num % i == 0:
            lst.append(i)
    return lst


n = int(input("Enter any number : "))
primes = find_prime(n)

if primes == []:
    print(f"{n} is a prime number. The prime numbers don't have prime factors.\nThank you!!")
else:
    print(f"Prime factors of {n} are = \n{primes} ")
