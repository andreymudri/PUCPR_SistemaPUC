class AcademicService:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        return self.students

    def remove_student(self, email):
        self.students = [s for s in self.students if s.email != email]

    def list_students(self):
        return self.students
