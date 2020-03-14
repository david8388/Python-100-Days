# 1. swap values

a = 6
b = 4
a, b = b, a
print('a = ', a, ' b = ', b)


# 2. check if the given number is even

def is_even(num):
    return num % 2 == 0


print(is_even(20))


# 3. split a multiline string into a list of lines

def split_lines(s):
    return s.split('\n')


print(split_lines('This is\n python\n data'))


# 4. reverse a string

language = 'python'

reversed_language = language[::-1]

print(reversed_language)

# 5. print a string n times


def repeat(string , n):
    return string * n


print(repeat('Hi', 5))
