def encrypt(letter, s):
    if (letter.isupper()):
        return chr((ord(letter) + s - 65) %
                   26 + 65)  # for uppercase input string
    elif (letter.islower()):
        # for smallercase input string
        return chr((ord(letter) + s - 97) % 26 + 97)
    else:
        return letter


text = input("Enter the word: ")
s = int(input("Enter the shift: "))
# shifts the alphabet by input spaces in the english alphabet
shift = [s] * len(text)
result = list(map(encrypt, text, shift))

print("Encrypted text: ", end="")
for i in result:
    print(i, end="")
