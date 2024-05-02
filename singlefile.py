'''
Nome: Andrey Beckert Mudri
Curso: Análise e Desenvolvimento de Sistemas
'''
import json


def load_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return None

def save_json(filename, data):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")
    
def main():
    def get_data():
        return {
            "students": students,
            "teachers": teachers,
            "disciplines": disciplines,
            "classes": classes,
            "enrollments": enrollments
        }
    data = load_json('data.json')
    if data is not None:
        students = data.get('students', [])
        disciplines = data.get('disciplines', [])
        teachers = data.get('teachers', [])
        classes = data.get('classes', [])
        enrollments = data.get('enrollments', [])
    else:
        students = []
        disciplines = []
        teachers = []
        classes = []
        enrollments = []

    while True:
        print("\n\n---- MENU PRINCIPAL ----")
        print("1. Menu de Estudantes")
        print("2. Menu de Disciplinas")
        print("3. Menu de Professores")
        print("4. Menu de Turmas")
        print("5. Menu de Matrículas")
        print("6. Sair")
        option = input("\nDigite a opção desejada: ") # entrada
        
        if option == "1":
            print("\n\n---- MENU DE ESTUDANTES ----") #Menu de estudantes
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
                    code = int(input("Digite o código do estudante: "))
                    name = input("Digite o nome do estudante: ")
                    CPF = input("Digite o CPF do estudante: ")
                    student = {"code": code, "name": name, "CPF": CPF}
                    students.append(student)
                    save_json('data.json', get_data())
                    print(f"Estudante {student['name']} cadastrado com sucesso!")
                elif option == "2":
                    print("Listar Estudantes")
                    print("Lista de Estudantes:")
                    for student in students:
                        print(f"Nome: {student['name']} - CPF: {student['CPF']}")
                elif option == "3":
                    print("Excluir Estudante")
                    code = int(input("Digite o código do estudante que deseja excluir: "))
                    students = [s for s in students if s["code"] != code]
                    save_json('data.json', get_data())
                elif option == "4":
                    print("Editar Estudante")
                    code = int(input("Digite o código do estudante que deseja editar: "))
                    for student in students:
                        if student["code"] == code:
                            new_code = int(input("Digite o novo code: "))
                            student["code"] = new_code
                            save_json('data.json', get_data())
                            print(f"Estudante {student['name']} editado com sucesso!")
                            break
                    else:
                        print("Estudante não encontrado")
                elif option == "5":
                    print("Voltar ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
            
        elif option == "2":
            print("\n\n---- MENU DE DISCIPLINAS ----") #Menu de disciplinas
            while True:
                print("\n\nMenu de Disciplinas:")
                print("1. Cadastrar Disciplina")
                print("2. Listar Disciplinas")
                print("3. Excluir Disciplina")
                print("4. Editar Disciplina")
                print("5. Voltar ao menu principal")
                option = input("\nDigite a opção desejada: ")
                if option == "1":
                    print("Cadastrar Disciplina")
                    code = int(input("Digite o código da disciplina: "))
                    name = input("Digite o nome da disciplina: ")
                    discipline = {"code": code, "name": name}
                    disciplines.append(discipline)
                    save_json('data.json', get_data())
                    print(f"Disciplina {discipline['name']} cadastrada com sucesso!")
                elif option == "2":
                    print("Listar Disciplinas")
                    print("Lista de Disciplinas:")
                    for discipline in disciplines:
                        print(f"Nome: {discipline['name']} - Código: {discipline['code']}")
                elif option == "3":
                    print("Excluir Disciplina")
                    code = int(input("Digite o código da disciplina que deseja excluir: "))
                    disciplines = [d for d in disciplines if d["code"] != code]
                    save_json('data.json', get_data())
                elif option == "4":
                    print("Editar Disciplina")
                    code = int(input("Digite o código da disciplina que deseja editar: "))
                    for discipline in disciplines:
                        if discipline["code"] == code:
                            new_code = int(input("Digite o novo código: "))
                            discipline["code"] = new_code
                            save_json('data.json', get_data())
                            print(f"Disciplina {discipline['name']} editada com sucesso!")
                            break
                    else:
                        print("Disciplina não encontrada")
                elif option == "5":
                    print("Voltar ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        elif option == "3":
            print("\n\n---- MENU DE PROFESSORES ----") #Menu de professores
            while True:
                print("\n\nMenu de Professores:")
                print("1. Cadastrar Professor")
                print("2. Listar Professores")
                print("3. Excluir Professor")
                print("4. Editar Professor")
                print("5. Voltar ao menu principal")
                option = input("\nDigite a opção desejada: ")
                if option == "1":
                    print("Cadastrar Professor")
                    code = int(input("Digite o código do professor: "))
                    name = input("Digite o nome do professor: ")
                    CPF = input("Digite o CPF do professor: ")
                    teacher = {"code": code, "name": name, "CPF": CPF}
                    teachers.append(teacher)
                    save_json('data.json', get_data())
                    print(f"Professor {teacher['name']} cadastrado com sucesso!")
                elif option == "2":
                    print("Listar Professores")
                    print("Lista de Professores:")
                    for teacher in teachers:
                        print(f"Nome: {teacher['name']} - CPF: {teacher['CPF']}")
                elif option == "3":
                    print("Excluir Professor")
                    code = int(input("Digite o código do professor que deseja excluir: "))
                    teachers = [t for t in teachers if t["code"] != code]
                    save_json('data.json', get_data())
                elif option == "4":
                    print("Editar Professor")
                    code = int(input("Digite o código do professor que deseja editar: "))
                    for teacher in teachers:
                        if teacher["code"] == code:
                            new_code = int(input("Digite o novo código: "))
                            teacher["code"] = new_code
                            save_json('data.json', get_data())
                            print(f"Professor {teacher['name']} editado com sucesso!")
                            break
                    else:
                        print("Professor não encontrado")
                elif option == "5":
                    print("Voltar ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        elif option == "4":
            print("\n\n---- MENU DE TURMAS ----") #Menu de turmas
            while True:
                print("\n\nMenu de Turmas:")
                print("1. Cadastrar Turma")
                print("2. Listar Turmas")
                print("3. Excluir Turma")
                print("4. Editar Turma")
                print("5. Voltar ao menu principal")
                option = input("\nDigite a opção desejada: ")
                if option == "1":
                    print("Cadastrar Turma")
                    name = input("Digite o nome da turma: ")
                    code = int(input("Digite o código da turma: "))
                    class_ = {"name": name, "code": code}
                    classes.append(class_)
                    save_json('data.json', get_data())
                    print(f"Turma {class_['name']} cadastrada com sucesso!")
                elif option == "2":
                    print("Listar Turmas")
                    print("Lista de Turmas:")
                    for class_ in classes:
                        print(f"Nome: {class_['name']} - Código: {class_['code']}")
                elif option == "3":
                    print("Excluir Turma")
                    code = int(input("Digite o código da turma que deseja excluir: "))
                    classes = [c for c in classes if c["code"] != code]
                    save_json('data.json', get_data())
                elif option == "4":
                    print("Editar Turma")
                    code = int(input("Digite o código da turma que deseja editar: "))
                    for class_ in classes:
                        if class_["code"] == code:
                            new_code = int(input("Digite o novo código: "))
                            class_["code"] = new_code
                            save_json('data.json', get_data())
                            print(f"Turma {class_['name']} editada com sucesso!")
                            break
                    else:
                        print("Turma não encontrada")
                elif option == "5":
                    print("Voltar ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        elif option == "5":
            print("\n\n---- MENU DE MATRÍCULAS ----") #Menu de matrículas
            while True:
                print("\n\nMenu de Matrículas:")
                print("1. Cadastrar Matrícula")
                print("2. Listar Matrículas")
                print("3. Excluir Matrícula")
                print("4. Editar Matrícula")
                print("5. Voltar ao menu principal")
                option = input("\nDigite a opção desejada: ")
                if option == "1":
                    print("Cadastrar Matrícula")
                    student_CPF = input("Digite o CPF do estudante: ")
                    discipline_code = int(input("Digite o código da disciplina: "))
                    enrollment = {"student_CPF": student_CPF, "discipline_code": discipline_code}
                    enrollments.append(enrollment)
                    save_json('data.json', get_data())
                    print(f"Matrícula do estudante {enrollment['student_CPF']} na disciplina {enrollment['discipline_code']} cadastrada com sucesso!")
                elif option == "2":
                    print("Listar Matrículas")
                    print("Lista de Matrículas:")
                    for enrollment in enrollments:
                        print(f"CPF do Estudante: {enrollment['student_CPF']} - Código da Disciplina: {enrollment['discipline_code']}")
                elif option == "3":
                    print("Excluir Matrícula")
                    student_CPF = input("Digite o CPF do estudante da matrícula que deseja excluir: ")
                    discipline_code = int(input("Digite o código da disciplina da matrícula que deseja excluir: "))
                    enrollments = [e for e in enrollments if e["student_CPF"] != student_CPF or e["discipline_code"] != discipline_code]
                    save_json('data.json', get_data())
                elif option == "4":
                    print("Editar Matrícula")
                    student_code = int(input("Digite o código do estudante da matrícula que deseja editar: "))
                    discipline_code = int(input("Digite o código da disciplina da matrícula que deseja editar: "))
                    for enrollment in enrollments:
                        if enrollment["student_code"] == student_code and enrollment["discipline_code"] == discipline_code:
                            new_student_code = int(input("Digite o novo código do estudante: "))
                            new_discipline_code = int(input("Digite o novo código da disciplina: "))
                            enrollment["student_code"] = new_student_code
                            enrollment["discipline_code"] = new_discipline_code
                            save_json('data.json', get_data())
                            print(f"Matrícula do estudante {enrollment['student_cod1e']} na disciplina {enrollment['discipline_code']} editada com sucesso!")
                            break
                    else:
                        print("Matrícula não encontrada")
                elif option == "5":
                    print("Voltar ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        elif option == "6":
            print("Saindo do sistema...\n")
            save_json('data.json', get_data())
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()