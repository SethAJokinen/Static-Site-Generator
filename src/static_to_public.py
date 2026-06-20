import shutil, os
from pathlib import Path

def static_to_public(from_path, to_path):
        if not os.path.exists(to_path):
            os.mkdir(to_path)
        for item in from_path.iterdir():
            if item.is_file():
                shutil.copy(item, to_path)
            elif item.is_dir():
                static_to_public(item, os.path.join(to_path, item.name))
    