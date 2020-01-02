class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def play(self):
        if self.__age <= 16:
            print('%s正在玩風箏' % self.__name)
        else:
            print('%s在玩桌遊' % self.__name)


def main():
    person = Person('David', 15)
    person.play()
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()
