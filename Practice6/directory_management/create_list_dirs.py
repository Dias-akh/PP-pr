from pathlib import Path

folder = Path('test_folder')
folder.mkdir(exist_ok=True)

print(f"Содержимое {Path.cwd().name}:")
for item in Path('.').iterdir():
    type_name = "DIR" if item.is_dir() else "FILE"
    print(f"[{type_name}] {item.name}")