
from services.menu.student_menu import show_student_menu


def show_menu():
    print("\n\n---- MENU PRINCIPAL ----")
    print("1. Menu de Estudantes")
    print("2. Menu de Disciplinas")
    print("3. Menu de Professores")
    print("4. Menu de Turmas")
    print("5. Menu de Matrículas")
    print("6. Sair")

def main():
    while True:
        show_menu()
        option = input("\n Digite a opção desejada: ")
        if option == "1":
            print("Menu de Estudantes selecionada")
            show_student_menu()
            
        elif option == "2":
            print("Menu de Disciplinas selecionada")
            
        elif option == "3":
            print("Menu de Professores selecionada")
            
        elif option == "4":
            print("Menu de Turmas selecionada")
            
        elif option == "5":
            print("Menu de Matrículas selecionada")
            
        elif option == "6":
            print("Saindo do sistema...")
            break


if __name__ == "__main__":
    main()
