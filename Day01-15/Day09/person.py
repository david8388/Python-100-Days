class Person(object):

    # __slots__ = ('_name', '_age', '_gender') 限定Person class 只能綁定 name, age, gender

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s 正在愉快玩耍' % self._name)

    def watch_av(self):
        if self._age >= 16:
            print('%s正在看AV' % self._name)
        else:
            print('%s不能看AV' % self._name)


def main():
    stu = Student('Luka', 15, '小三')
    stu.study('Math')
    stu.watch_av()
    t = Teacher('David', 25, 'Python 100天')
    t.teach('Python')
    t.watch_av()
    # person = Person('David', 15)
    # person.play()
    # person.age = 22
    # person.play()
    # person._gender = 'man'
    # person._isSales = False # AttributeError: 'Person' object has no attribute '_isSales'


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在學習%s' % (self._grade, self._name, course))


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在講%s' % (self._name, self._title, course))


if __name__ == '__main__':
    main()
