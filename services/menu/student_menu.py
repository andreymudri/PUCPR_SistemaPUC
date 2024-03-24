def student_menu():
    while True:
        print("\n\nMenu de Estudantes:")
        print("1. Cadastrar Estudante")
        print("2. Listar Estudantes")
        print("3. Excluir Estudante")
        print("4. Voltar ao menu principal")
        option = input("\nDigite a opção desejada: ")
        if option == "1":
            print("Cadastrar Estudante")
        elif option == "2":
            print("Listar Estudantes")
        elif option == "3":
            print("Excluir Estudante")
        elif option == "4":
            print("Voltar ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")