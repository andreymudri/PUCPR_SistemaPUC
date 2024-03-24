def class_menu():

    while True:
        print("\n\nMenu de Turmas:")
        print("1. Cadastrar Turma")
        print("2. Listar Turmas")
        print("3. Excluir Turma")
        print("4. Voltar ao menu principal")
        option = input("\nDigite a opção desejada: ")
        if option == "1":
            print("Cadastrar Turma")
        elif option == "2":
            print("Listar Turmas")
        elif option == "3":
            print("Excluir Turma")
        elif option == "4":
            print("Voltar ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")