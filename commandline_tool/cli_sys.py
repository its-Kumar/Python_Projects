import sys

if __name__ == "__main__":
    try:
        name = sys.argv[1]
    except:
        name = input("What is your name?")
    from getpass import getpass

    pw = getpass("what is your password?")
    print(f"{name=}, {pw=}")
