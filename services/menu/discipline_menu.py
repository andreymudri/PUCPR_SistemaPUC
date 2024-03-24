def discipline_menu():
    while True:
        print("\n\nMenu de Disciplinas:")
        print("1. Cadastrar Disciplina")
        print("2. Listar Disciplinas")
        print("3. Excluir Disciplina")
        print("4. Voltar ao menu principal")
        option = input("\nDigite a opção desejada: ")
        if option == "1":
            print("Cadastrar Disciplina")
        elif option == "2":
            print("Listar Disciplinas")
        elif option == "3":
            print("Excluir Disciplina")
        elif option == "4":
            print("Voltar ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")