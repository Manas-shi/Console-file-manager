import os
import shutil
import sys


def find_folder_by_name(root_path, folder_or_file_name):
    for dirpath, dirnames, filenames in os.walk(root_path):
        if folder_or_file_name in dirnames:
            folder_path = os.path.join(dirpath, folder_or_file_name)
            return folder_path
        elif folder_or_file_name in filenames:
            file_path = os.path.join(dirpath, folder_or_file_name)
            return file_path
    return None

def create_new_folder(root_path=None, folder_to_find=None, use_custom_directory=True, use_current_directory=False):
    if use_current_directory:
        folder_path = os.getcwd()
        new_folder_name = input("Введите название новой папки: ")
        new_folder_path = os.path.join(folder_path, new_folder_name)
        os.makedirs(new_folder_path, exist_ok=True)
        print(f"Папка '{new_folder_name}' успешно создана в текущей директории '{folder_path}'.")
    elif use_custom_directory and folder_to_find:
        folder_path = find_folder_by_name(root_path, folder_to_find)
        if folder_path:
            new_folder_name = input("Введите название новой папки: ")
            new_folder_path = os.path.join(folder_path, new_folder_name)
            os.makedirs(new_folder_path, exist_ok=True)
            print(f"Папка '{new_folder_name}' успешно создана в '{folder_path}'.")
        else:
            print(f"Папка '{folder_to_find}' не найдена.")
    elif not use_custom_directory:
        new_folder_name = input("Введите название новой папки: ")
        folder_path = r"C:\\"
        new_folder_path = os.path.join(folder_path, new_folder_name)
        os.makedirs(new_folder_path, exist_ok=True)
        print(f"Папка '{new_folder_name}' успешно создана на диске C.")

def delete_folder_or_file(name, root_directory, delete_all=False, is_file=False):
    if delete_all:
        found = False
        for dirpath, dirnames, filenames in os.walk(root_directory):
            if is_file and name in filenames:
                file_path = os.path.join(dirpath, name)
                if confirm_deletion(file_path):
                    os.remove(file_path)
                    print(f"Файл '{name}' удален по пути: {file_path}")
                    found = True
            elif not is_file and name in dirnames:
                folder_path = os.path.join(dirpath, name)
                if confirm_deletion(folder_path):
                    shutil.rmtree(folder_path)
                    print(f"Папка '{name}' удалена по пути: {folder_path}")
                    found = True
        if not found:
            print(f"{'Файл' if is_file else 'Папка'} с именем '{name}' не найдена.")
    else:
        current_directory = os.getcwd()
        item_path = find_folder_by_name(current_directory, name)
        if item_path:
            if is_file and os.path.isfile(item_path):
                if confirm_deletion(item_path):
                    os.remove(item_path)
                    print(f"Файл '{name}' успешно удален из рабочей директории.")
            elif not is_file and os.path.isdir(item_path):
                if confirm_deletion(item_path):
                    shutil.rmtree(item_path)
                    print(f"Папка '{name}' успешно удалена из рабочей директории.")
        else:
            print(f"{'Файл' if is_file else 'Папка'} '{name}' не найдена в рабочей директории.")

def confirm_deletion(path):
    confirmation = input(f"Вы уверены, что хотите удалить '{path}'? (y/n): ").lower()
    if confirmation == 'y':
        return True
    else:
        print(f"Удаление '{path}' отменено.")
        return False

def copy_folder_file(item_name, root_directory):
    item_path = find_folder_by_name(root_directory, item_name)
    if not item_path:
        print(f"Файл или папка '{item_name}' не найдены.")
        return

    destination_folder = input("Введите название папки, куда нужно скопировать: ")
    destination_path = find_folder_by_name(root_directory, destination_folder)

    if not destination_path:
        print(f"Папка назначения '{destination_folder}' не найдена.")
        return

    if os.path.isfile(item_path):
        shutil.copy(item_path, destination_path)
        print(f"Файл '{item_name}' успешно скопирован в '{destination_path}'.")

    elif os.path.isdir(item_path):
        new_folder_path = os.path.join(destination_path, os.path.basename(item_path))
        shutil.copytree(item_path, new_folder_path)
        print(f"Папка '{item_name}' успешно скопирована в '{destination_path}'.")
    else:
        print(f"Неизвестный тип объекта '{item_name}'.")


def view_working_directory_contents():
    return sys.path


def view_only_folders():
    current_directory = os.getcwd()
    print(f"Текущая рабочая директория: {current_directory}")

    contents = os.listdir(current_directory)

    folders = [item for item in contents if os.path.isdir(os.path.join(current_directory, item))]

    if not folders:
        print("Папок нет.")
    else:
        print("Папки в текущей рабочей директории:")
        for folder in folders:
            print(folder)

def view_only_files():
    current_directory = os.getcwd()
    print(f"Текущая рабочая директория: {current_directory}")

    contents = os.listdir(current_directory)

    files = [item for item in contents if os.path.isfile(os.path.join(current_directory, item))]

    if not files:
        print("Файлов нет.")
    else:
        print("Файлы в текущей рабочей директории:")
        for file in files:
            print(file)

def system_info_sys():
    print("Информация о системе с использованием sys:")
    print(f"Платформа: {sys.platform}")
    print(f"Версия Python: {sys.version}")
    print(f"Путь к интерпретатору Python: {sys.executable}")

    if sys.platform == "win32":
        windows_version = sys.getwindowsversion()
        print(f"Версия Windows: {windows_version.major}.{windows_version.minor}")
        print(f"Сборка: {windows_version.build}")
        print(f"Сервис-пак: {windows_version.service_pack}")

def show_creator_info():
    creator_info = {
        "Имя": "Сыдыков Манарбек",
        "Email": "dr.manarbek@gmail.com",
        "Версия программы": "1.0.0",
        "Описание": "Эта программа позволят работать с операционной системой."
    }
    print("Информация о создателе программы:")
    for key, value in creator_info.items():
        print(f"{key}: {value}")

def change_working_directory():
    user_input = input("Введите новый путь к рабочей директории: ")
    folder_path = find_folder_by_name(root_directory, user_input)
    if folder_path:
        new_directory = os.path.join(folder_path)
        os.chdir(new_directory)
        print(f"Рабочая директория успешно изменена на: {os.getcwd()}")
    if not folder_path:
        print(f"Директории {user_input} не существует.")


