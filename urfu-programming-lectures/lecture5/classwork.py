class Student:
    def __init__(self, age: int, name: str, is_cool: bool) -> None:
        self.age = age
        self.name = name
        self.is_cool = is_cool

    def change_cool(self, status: bool) -> str:
        self.is_cool = status
        if status:
            return "ты крут"
        else:
            return "ты не крут"

    def edit_age(self, new_age: int) -> str:
        self.age = new_age
        return "Повзрослел братик"

    def hello_student(self) -> str:
        return f"Круто поступил, {self.name}"


class Teacher:
    def __init__(self, name: str, lesson: str, is_kind: bool) -> None:
        self.name = name
        self.lesson = lesson
        self.is_kind = is_kind
        self.students = []

    def be_angry(self) -> str:
        self.is_kind = False
        return "стал злым"

    def edit_lesson(self, new_lesson: str) -> str:
        self.lesson = new_lesson
        return f"установлен новый предмет {new_lesson}"

    def add_student(self, student_d: Student) -> None:
        self.students.append(student_d)

    def get_students(self) -> list | str:
        if not self.students:
            return "у него нет студентов"
        return self.students


i_am = Student(18, "alexander", True)
print(i_am.is_cool)
i_am.change_cool(False)
print(i_am.is_cool)
print(i_am.hello_student())

t1 = Teacher("vadim", "coding", True)
print(t1.be_angry())

print(t1.get_students())
t1.add_student(i_am)

if t1.get_students():
    for student in t1.get_students():
        print(f"имя студента: {student.name}")
