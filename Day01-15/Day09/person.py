class Person(object):

    __slots__ = ('_name', '_age', '_gender')

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
        if self._age <= 16:
            print('%s正在玩風箏' % self._name)
        else:
            print('%s在玩桌遊' % self._name)


def main():
    person = Person('David', 15)
    person.play()
    person.age = 22
    person.play()
    person._gender = 'man'
    # person._isSales = False # AttributeError: 'Person' object has no attribute '_isSales'


if __name__ == '__main__':
    main()
