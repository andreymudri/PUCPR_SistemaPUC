def enrollment_menu():
    while True:
        print("\n\nMenu de Matrículas:")
        print("1. Matricular Aluno")
        print("2. Listar Matrículas")
        print("3. Excluir Matrícula")
        print("4. Voltar ao menu principal")
        option = input("\nDigite a opção desejada: ")
        if option == "1":
            print("Matricular Aluno")
        elif option == "2":
            print("Listar Matrículas")
        elif option == "3":
            print("Excluir Matrícula")
        elif option == "4":
            print("Voltar ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
