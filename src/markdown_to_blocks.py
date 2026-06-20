
def markdown_to_blocks(markdown):
    md_finished_list = []
    md_list = markdown.split("\n\n")
    for item in md_list:
        new_item = item.strip()
        if new_item:
            md_finished_list.append(new_item)
    
    return md_finished_list