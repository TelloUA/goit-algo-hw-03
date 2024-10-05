import argparse
import os
import shutil
from pathlib import Path

counter = 0

def main() -> None:
    source_dir, destination_dir = parse_args()

    # Перевірка на валідність папки звідки відбувається копіювання
    if not is_valid_source_dir(source_dir):
        print('Source argument required or directory not exist')
        return
    else:
        source = Path(source_dir)

    # Створення папки призначення
    dst = create_destination_dir(destination_dir)

    # Сам процес копіювання файлів
    copy_files(source, dst)
    print(f"Success operation, copied {counter} files")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", type=str)
    parser.add_argument("-d", "--destination", type=str, default="dist")
    args = parser.parse_args()

    return args.source, args.destination

def is_valid_source_dir(path):    
    return path is not None and os.path.exists(path)

def create_destination_dir(path: str) -> Path:
    destination = Path(path)
    destination.mkdir(parents=True, exist_ok=True) 
    return destination

def create_extesion_dir(destination: Path, extension: str) -> Path:
    folder = destination / extension
    folder.mkdir(exist_ok=True)
    return folder

def copy_files(path: Path, destination: Path) -> None:    
    global counter

    # Якщо папка - запускаємо функцію ще раз
    if path.is_dir():
        for child in path.iterdir():
            copy_files(child, destination)

    # Якщо файл - створюємо папку та копіюємо
    # Обробити помилку доступу до файлу
    else:
        if os.access(path, os.R_OK):
            folder_destination = create_extesion_dir(destination, path.suffix[1:])
            shutil.copy(path, folder_destination)
            counter += 1
        else:
            print(f"No access to {path.name}")

def change_access() -> None:
    file_path = Path('pictures/test.jpeg')
    # file_path.chmod(0o000)
    # file_path.chmod(0o644)

if __name__ == "__main__":
    main()
    # change_access()