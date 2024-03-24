def teachers_menu():
    while True:
        print("\n\nMenu de Professores:")
        print("1. Cadastrar Professor")
        print("2. Listar Professores")
        print("3. Excluir Professor")
        print("4. Voltar ao menu principal")
        option = input("\nDigite a opção desejada: ")
        if option == "1":
            print("Cadastrar Professor")
        elif option == "2":
            print("Listar Professores")
        elif option == "3":
            print("Excluir Professor")
        elif option == "4":
            print("Voltar ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
