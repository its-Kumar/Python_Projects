# gunicorn server
import views


def app(environ, start_response):
    path = environ.get("PATH_INFO")
    if path.endswith("/"):
        path = path[:-1]
    if path == "":  # index / root of the web
        data = views.home(environ)
    elif path == "/contact":
        data = views.contact_us(environ)
    else:
        data = views.render_template("error.html", context={"path": path})

    # data = "Hello World!"
    data = data.encode("utf-8")
    start_response(
        f"200 OK",
        [
            # ("Content-Type", "text/plain"),
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data))),
        ],
    )
    return iter([data])
