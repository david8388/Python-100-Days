class User:
    def __init__(self, name, age, country):
        # public
        self.name = name
        # start with __ is private
        self.__age = age
        # start with _ is protected
        self._country = country

    # public func
    def sayHi(self):
        print('Hi, my name is {0}'.format(self.name))

    # private func
    def __getAge(self):
        print(self.__age)

    # protected func
    def _getCountry(self):
        print(self._country)


a = User('David', '25', 'Taiwan')
print(a.name, a.sayHi())
# print(a.__age) AttributeError: 'User' object has no attribute '__age', prop is private so can't access.
# print(a._getAge()) # AttributeError: 'User' object has no attribute '_getAge'
print(a._country, a._getCountry())