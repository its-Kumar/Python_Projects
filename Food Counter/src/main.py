import os
from src import init_api

HOST = os.getenv("IP_ADDRESS") or "127.0.0.1"


def main():
    app = init_api()
    app.run(host=HOST, port=8080)


if __name__ == "__main__":
    main()