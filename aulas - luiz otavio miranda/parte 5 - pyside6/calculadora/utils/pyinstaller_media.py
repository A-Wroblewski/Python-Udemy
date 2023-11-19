import os
import sys

from images_paths import IMAGES_DIR_PATH

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(IMAGES_DIR_PATH)

    return os.path.join(base_path, relative_path)
