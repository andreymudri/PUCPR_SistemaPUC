
from services.menu.class_menu import show_class_menu
from services.menu.discipline_menu import show_discipline_menu
from services.menu.enrollment_menu import show_enrollment_menu
from services.menu.student_menu import show_student_menu
from services.menu.teachers_menu import show_teachers_menu


def show_menu():
    print("\n\n---- MENU PRINCIPAL ----")
    print("1. Menu de Estudantes")
    print("2. Menu de Disciplinas")
    print("3. Menu de Professores")
    print("4. Menu de Turmas")
    print("5. Menu de Matrículas")
    print("6. Sair")

def main():
    menu_options = {
        "1": show_student_menu,
        "2": show_discipline_menu,
        "3": show_teachers_menu,
        "4": show_class_menu,
        "5": show_enrollment_menu,
    }

    while True:
        show_menu()
        option = input("\n Digite a opção desejada: ")

        if option in menu_options:
            print(f"Menu {menu_options[option].__name__} selecionada")
            menu_options[option]()
        elif option == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
