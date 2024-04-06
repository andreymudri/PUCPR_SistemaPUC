from models.student import Student



def student_menu(academic_service):
    student1 = Student("nome", "email")
    academic_service.add_student(student1)
    while True:
        print("\n\nMenu de Estudantes:")
        print("1. Cadastrar Estudante")
        print("2. Listar Estudantes")
        print("3. Excluir Estudante")
        print("4. Editar Estudante")
        print("5. Voltar ao menu principal")
        option = input("\nDigite a opção desejada: ")
        if option == "1":
            print("Cadastrar Estudante")
            name = input("Digite o nome do estudante: ")
            email = input("\nDigite o email do estudante: ")
            student = Student(name, email)
            print(f"Estudante {student.name} cadastrado com sucesso!")
            academic_service.add_student(student)
            
        elif option == "2":
            print("Listar Estudantes")
            student_list = academic_service.list_students()
            print("Lista de Estudantes:")
            for student in student_list:
                print(f"Nome: {student.name} - Email: {student.email}")
                
        elif option == "3":
            print("Excluir Estudante")
            email = input("Digite o email do estudante que deseja excluir: ")
            academic_service.remove_student(email)
        elif option == "4":
            print("Editar Estudante")
            email = input("Digite o email do estudante que deseja editar: ")
            student = academic_service.get_student(email)
            if student:
                new_email = input("Digite o novo email: ")
                academic_service.edit_student(student, new_email)
                print(f"Estudante {student.name} editado com sucesso!")
            else:
                print("Estudante não encontrado")
            
        elif option == "5":
            print("Voltar ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")