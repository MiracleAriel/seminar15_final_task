import os
import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Создаем объект namedtuple для хранения информации о содержимом
DirectoryEntry = namedtuple('DirectoryEntry', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_directory_info(directory_path):
    # Проверяем, что указанный путь действительно является директорией
    if not os.path.isdir(directory_path):
        logging.error(f"Path {directory_path} is not a valid directory.")
        return

    directory_entries = []

    # Обходим директорию и собираем информацию о каждом элементе
    for entry in os.scandir(directory_path):
        name = os.path.splitext(entry.name)[0]
        extension = os.path.splitext(entry.name)[1].lstrip('.')
        is_directory = entry.is_dir()
        parent_directory = os.path.basename(directory_path)

        directory_entry = DirectoryEntry(name, extension, is_directory, parent_directory)
        directory_entries.append(directory_entry)

        logging.info(f"Entry: {name}, Extension: {extension}, Is Directory: {is_directory}, Parent Directory: {parent_directory}")

    return directory_entries

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python script_name.py directory_path")
        sys.exit(1)

    directory_path = sys.argv[1]
    directory_info = get_directory_info(directory_path)

    if directory_info:
        print("Directory content information:")
        for entry in directory_info:
            print(entry)
