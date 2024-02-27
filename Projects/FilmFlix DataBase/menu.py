import read, add, updateOneField, updateAllFields, delete, search

def read_file(file_path):
    try:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as fileNotFound:
        print(f"File not found: {fileNotFound}")

def film_menu():
    option = 0
    optionsList = ["1", "2", "3", "4", "5", "6", "7"]

    menu_choices = read_file("Week 11 - Python Project/FilmFlix DataBase/menuOptions.txt")

    while option not in optionsList:
        print(" ╭──────────────────────────╮")
        print(menu_choices)
        print(" ╰──────────────────────────╯")
        print("")
        option = input("Enter an option from the menu choice above: ")
        print("")

        if option not in optionsList:
            print(f"{option} is not a valid choice!")
    return option

mainProgram = True

while mainProgram:
    main_menu = film_menu()

    match main_menu:
        case "1":
            read.all_films()
        case "2":
            add.insert_film()
        case "3":
            updateOneField.update_one_field()
        case "4":
            updateAllFields.update_all_fields()
        case "5":
            delete.delete_film()
        case "6":
            search.search_film()
        case "7":
            mainProgram = False

print("Program closed")
