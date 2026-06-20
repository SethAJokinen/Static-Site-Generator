from pathlib import Path
import shutil, os
from static_to_public import static_to_public
from generate_page import generate_page, generate_pages_recursive
import sys


def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"
    public_path = Path("./public")
    if os.path.exists(public_path):
        for item in public_path.iterdir():
            if item.is_file() or item.is_symlink():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)

    static_path = Path("./static")
    static_to_public(static_path, public_path)
    generate_pages_recursive("./content", "./template.html", "./docs", base_path)
main()