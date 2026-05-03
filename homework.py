from pathlib import Path
import re

base = Path(__file__).parent
file_path = base / "developers_salary.txt"

def total_salary(path: Path) -> tuple:
    
    if not path.exists():
        return None
    
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        all_salaries = [int(n) for n in re.findall(r"\d+", text)]
        sum_salary = sum(all_salaries)
        average_salary = sum_salary / len(all_salaries)
        return sum_salary, average_salary

print(total_salary(file_path))