from pathlib import Path
import sys
from colorama import init, Fore


init(autoreset=True)

def visualize_tree(path: Path) -> None:    
    for item in path.iterdir():
        if item.is_dir():
            print(" " + Fore.BLUE + f"{item.name}")
            visualize_tree(item)
        else:
            print("  " + Fore.GREEN + f"{item.name}")


if len(sys.argv) > 1:
    file_path = Path(sys.argv[1])

if file_path.exists() and file_path.is_dir():
    visualize_tree(file_path)
else:
    print(Fore.RED + "Помилка: Шлях не знайдено або це не директорія.")
