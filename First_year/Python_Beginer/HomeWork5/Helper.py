import os


def check_exist_file(file_path):
    if not os.path.exists(file_path):
        print('Файл не найден')
        exit(0)