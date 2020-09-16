def is_prime(num):

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False

    return True


def prime_gen(current_prime):

    next_prime = current_prime + 1

    while True:

        if not is_prime(next_prime):
            next_prime += 1

        else:
            break
    return next_prime


current_prime = 2
while True:

    answer = input('Would you like to see the next prime? (Y/N) ')

    if answer[0].lower() == 'y':
        print(current_prime)
        current_prime = prime_gen(current_prime)

    else:
        break

print("Thanks..!!")
