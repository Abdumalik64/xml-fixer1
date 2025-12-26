import os

REPLACEMENTS = {
    "Ќ": "Қ", "ќ": "қ",
    "Љ": "Ҷ", "љ": "ҷ",
    "Њ": "Ҳ", "њ": "ҳ",
    "Ў": "Ӯ", "ў": "ӯ",
    "Ѓ": "Ғ", "ѓ": "ғ",
    "Ї": "Ӣ", "ї": "ӣ"
}

WORK_DIR = os.getcwd()

def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    for old, new in REPLACEMENTS.items():
        content = content.replace(old, new)

    new_path = os.path.splitext(path)[0] + "_fixed.xml"

    with open(new_path, "w", encoding="utf-8") as f:
        f.write(content)

for file in os.listdir(WORK_DIR):
    if file.lower().endswith(".xml"):
        fix_file(os.path.join(WORK_DIR, file))