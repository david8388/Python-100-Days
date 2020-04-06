class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


teacher = Person('David Wu', 26)
student1 = Person('May', 25)

print('teacher', teacher.name, teacher.age)
print('student1', student1.name, student1.age, student1.birthday(), student1.age)


