import json
import os
from pathlib import Path

# カレントディレクトリ内でスニペットを作成する。
def create_snipets():
    snippets = {}
    for file in Path(".").glob("*"):
        if not file.is_file(): continue
        basename, extension = file.stem, file.suffix[1:]
        if extension == 'json': continue

        with open(file, "r") as f:
            body = [line.strip().replace('"', '\\"') for line in f.readline()]
            body = [f'"{line}"' for line in body]
            
        snippets[basename] = {
            "prefix": basename,
            "body": body,
            "description": f"snipet for {basename}"
        }
    
    with open("snippets.json", "w") as f:
        json.dump(snippets, f, ensure_ascii=False, indent=4)

for folder in Path(".").glob("[a-z]+"):
    os.chdir(folder)
    create_snipets()
    os.chdir("..")