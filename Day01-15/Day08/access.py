class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test2 = Test('Foo')
    # test.__bar() # AttributeError: 'Test' object has no attribute '__bar'
    test2._Test__bar() # print Foo __bar
    # print(test.__foo) # AttributeError: 'Test' object has no attribute '__foo'
    print(test2._Test__foo) # print Foo


if __name__ == '__main__':
    main()
