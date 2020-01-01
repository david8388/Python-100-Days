class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在學習%s' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能看熊出沒.' % self.name)
        else:
            print('%s觀看愛情大電影' % self.name)


def main():
    stu1 = Student('Chia', 25)
    stu1.study('Python101')
    stu1.watch_movie()
    stu2 = Student('Luka', 17)
    stu2.study('Space Jam2')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
