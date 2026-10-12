class Student:
    def __init__(self, name, age, group, is_cool):
        self.name = name
        self.age = age
        self.group = group
        self.is_cool = is_cool

    def say_hello(self):
        print(f"я {self.name}, мне {self.age} лет.")

    def show_group(self):
        print(f"я учусь в группе {self.group}.")

    def cool(self, status):
        self.is_cool = status
        if status:
            print("теперь ты крутой")
        else:
            print("ты не оч")


student1 = Student("александр", 18, "группа", True)

print("имя:", student1.name)
print("возраст:", student1.age)
print("группа:", student1.group)
print("крутой:", student1.is_cool)
student1.cool(True)

student1.say_hello()
student1.show_group()
student1.cool(False)