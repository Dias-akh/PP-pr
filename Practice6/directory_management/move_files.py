from pathlib import Path

source = Path('sample.txt')
source.write_text("Hello Python", encoding='utf-8')

target_dir = Path('test_folder')
target_dir.mkdir(exist_ok=True)

destination = target_dir / source.name
source.rename(destination)

print(f"Moved {source} to {destination}")