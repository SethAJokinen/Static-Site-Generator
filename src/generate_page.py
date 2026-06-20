from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os
from pathlib import Path
import shutil

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
    with open(from_path) as content:
        from_content = content.read()
    
    with open(template_path) as content:
        template_content = content.read()
    
    html_content = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)

    html_title = template_content.replace(f"{{ Title }}", f"{title}")
    html_page = html_title.replace("{{ Content }}", f"{html_content}")
    href_and_src_replaced_html_page = html_page.replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as content:
        content.write(href_and_src_replaced_html_page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    content_dir = Path(dir_path_content)
    dest_dir = Path(dest_dir_path)

    for item in content_dir.iterdir():

        relative_path = item.relative_to(dir_path_content)
        corresponding_dest = dest_dir / relative_path

        if item.is_dir():
            generate_pages_recursive(item, template_path, corresponding_dest, base_path)

        elif item.is_file() and item.suffix == ".md":
            html_dest_path = corresponding_dest.with_suffix(".html")

            generate_page(str(item), str(template_path), str(html_dest_path), base_path)

        elif item.is_file():
            shutil.copy2(item, corresponding_dest)
