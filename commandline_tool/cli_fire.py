from getpass import getpass

import fire


def login(name=None):
    if name is None:
        name = input("What is your name?")
    pw = getpass("what is your password?")

    return f"{name=}, {pw=}"


if __name__ == "__main__":
    fire.Fire(login)
