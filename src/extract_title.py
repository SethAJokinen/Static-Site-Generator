
import re
def extract_title(markdown):
    lines = markdown.split("\n")
    header = ""
    for line in lines:
        if re.match(r"^# [^#]", line):
            header = line.lstrip().replace("# ", "")
    if header == "":
        raise Exception("No h1 heading found!")
    return header