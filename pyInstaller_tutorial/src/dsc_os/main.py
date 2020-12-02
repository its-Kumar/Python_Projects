import pathlib

from flask import Flask

from .resources import get_resources_path

BASE_DIR = pathlib.Path(__file__).resolve().parent
DATA_DIR = get_resources_path("data")
IMG_PATH = DATA_DIR / 'beach.jpeg'


web_app = Flask(__name__)


@web_app.route("/", methods=["GET"])
def index():
    return {"dir": str(BASE_DIR)}, 200
