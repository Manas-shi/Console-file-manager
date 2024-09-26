import work_with_OS
import sys
from use_functions import account_replenishment, purchase, purchase_history
from victory import victory as vc

root_directory = r"C:\\"

user_purchases = {}
user_account = 0

while True:
    print("Меню:")
    print("1. Создать папку")
    print("2. Удалить (файл / папку)")
    print("3. Копировать (файл / папку)")
    print("4. Просмотр содержимого рабочей директории")
    print("5. Посмотреть только папки")
    print("6. Посмотреть только файлы")
    print("7. Просмотр информации об операционной системе")
    print("8. Создатель программы")
    print("9. Играть в викторину")
    print("10. Мой банковский счет")
    print("11. Смена рабочей директории")
    print("12. Выход из программы.\n")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        while True:
            print("Меню:")
            print("1. Выбрать папку, где будет создана новая папка.")
            print("2. Создать папку на диске С.")
            print("3. Создать папку в текущей директории.")
            print("4. Выход из программы.\n")

            choice = input("Выберите пункт меню: ")

            if choice == "1":
                folder_to_work_with = input("Введите название папки, в которой нужно создать новую: ")
                work_with_OS.create_new_folder(root_directory, folder_to_work_with, use_custom_directory=True)

            elif choice == "2":
                work_with_OS.create_new_folder(use_custom_directory=False)

            elif choice == "3":
                work_with_OS.create_new_folder(use_current_directory=True)

            elif choice == "4":
                print("Выход из программы.")
                break

            else:
                print("Вы ввели неверные данные. Попробуйте снова.")

    elif choice == "2":
        item_name = input("Укажите название папки / файла, которые хотите удалить: ")

        while True:
            print("Меню:")
            print("1. Удалить папку в рабочей директории.")
            print("2. Удалить все одноименные папки во всех директориях.")
            print("3. Удалить только файл в рабочей директории.")
            print("4. Удалить все одноименные файлы во всех директориях.")
            print("5. Выход из программы.\n")

            choice = input("Выберите пункт меню: ")

            if choice == "1":
                work_with_OS.delete_folder_or_file(item_name, root_directory, delete_all=False, is_file=False)

            elif choice == "2":
                work_with_OS.delete_folder_or_file(item_name, root_directory, delete_all=True, is_file=False)

            elif choice == "3":
                work_with_OS.delete_folder_or_file(item_name, root_directory, delete_all=False, is_file=True)

            elif choice == "4":
                work_with_OS.delete_folder_or_file(item_name, root_directory, delete_all=True, is_file=True)

            elif choice == "5":
                print("Выход из программы.")
                break

            else:
                print("Вы ввели неверные данные. Попробуйте снова.")

    elif choice == "3":
        item_name = input("Введите название файла или папки, которую нужно скопировать: ")
        work_with_OS.copy_folder_file(item_name, r"C:\\")

    elif choice == "4":
        current_dir = work_with_OS.view_working_directory_contents()
        print(current_dir)

    elif choice == "5":
        work_with_OS.view_only_folders()

    elif choice == "6":
        work_with_OS.view_only_files()

    elif choice == "7":
        work_with_OS.system_info_sys()

    elif choice == "8":
        work_with_OS.show_creator_info()

    elif choice == "9":
        vc()

    elif choice == "10":
        while True:
            print("Меню:")
            print('1. пополнение счета')
            print('2. покупка')
            print('3. история покупок')
            print('4. выход')

            choice = input('Выберите пункт меню: ')
            if choice == '1':
                account_replenishment()
            elif choice == '2':
                purchase()
            elif choice == '3':
                purchase_history()
            elif choice == '4':
                break
            else:
                print('Неверный пункт меню')

    elif choice == "11":
        work_with_OS.change_working_directory()

    elif choice == "12":
        print("Выход из программы.")
        sys.exit()

    else:
        print("Вы ввели неверные данные. Попробуйте снова.")


