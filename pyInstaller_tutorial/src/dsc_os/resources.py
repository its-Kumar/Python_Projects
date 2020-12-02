import pathlib
import sys


def get_resources_path(relative_path):
    """get_resources_path

    Args:
        relative_path ([type]):  "data/beach.jpeg"
        relative_path ([type]):
        relative_path ([type]):
    """

    rel_path = pathlib.Path(relative_path)
    dev_bash_path = pathlib.Path(__file__).resolve().parent.parent
    base_path = getattr(sys, "_MEIPASS", dev_bash_path)
    return base_path / rel_path
