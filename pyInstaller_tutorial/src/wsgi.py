from waitress import serve

from dsc_os import web_app

if __name__ == "__main__":
    serve(
        web_app,
        host='127.0.0.1',
        port=5002,
        threads=2
    )
