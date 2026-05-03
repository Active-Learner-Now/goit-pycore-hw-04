from pathlib import Path
from typing import List, Dict

base = Path(__file__).parent
file_path = base / "cats_info.txt"

def get_cats_info(path: Path) -> List[Dict]:
    
    if not path.exists():
        return None
    
    cats_info_list = []
    
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        lines = text.splitlines()
        for line in lines:
            splited_line = line.split(",")
            records = {
                "id": splited_line[0],
                "name": splited_line[1],
                "age": splited_line[2]
            }
            cats_info_list.append(records)
        return cats_info_list
       

print(get_cats_info(file_path))