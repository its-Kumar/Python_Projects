# Python_webapp

A Pure Python Web Application Without using any FrameWork.


## Installation and Setup

1. install python 3.x
2. install requirements
`python -m pip install -r requirements.txt`
OR
`pip install -r requirements.txt`
3. if this did not worked than try `python -m pip install gunicorn`
4. run gunicorn server:
`gunicorn server:app --reload`
5. open the browser and go to the url which will apper
```bash
$ gunicorn server:app --reload
[2020-11-19 13:14:49 +0530] [14209] [INFO] Starting gunicorn 20.0.4
[2020-11-19 13:14:49 +0530] [14209] [INFO] Listening at: http://127.0.0.1:8000 (14209)
[2020-11-19 13:14:49 +0530] [14209] [INFO] Using worker: sync
[2020-11-19 13:14:49 +0530] [14212] [INFO] Booting worker with pid: 14212
```

## Templates

Put your templates/ html files in `templates` directory.

## Views

Put your views/ functions in `views.py` file


### App

Create a gunicorn web app using following function->

```python
def app(environ, start_response):
    #data = "Hello World!"
    data = views.home(environ)
    data = data.encode("utf-8")
    start_response(
        f"200 OK", [
            #("Content-Type", "text/plain"),
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])
```

### Developer
**[Kumar Shanu](https://its-kumar.github.io/)**
