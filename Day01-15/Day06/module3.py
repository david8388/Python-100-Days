def foo():
    pass

def bar():
    pass

print('main name', __name__)

if __name__ == "__main__":
    print('call foo()')
    foo()
    print('call bar()')
    bar()