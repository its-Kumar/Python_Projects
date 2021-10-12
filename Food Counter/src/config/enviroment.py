import os

DBHOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
HOST = os.getenv("IP_ADDRESS") or "localhost"
PORT = os.getenv("SERVER_PORT") or 8080