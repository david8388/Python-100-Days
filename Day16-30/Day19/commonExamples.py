from collections import Counter
import math

# 1. swap values

a = 6
b = 4
a, b = b, a
print('1. swap values ', 'a = ', a, ' b = ', b)


# 2. check if the given number is even

def is_even(num):
    return num % 2 == 0


print('2. check is even ', is_even(20))


# 3. split a multiline string into a list of lines

def split_lines(s):
    return s.split('\n')


print('3. multiline to a list ', split_lines('This is\n python\n data'))


# 4. reverse a string

language = 'python'

reversed_language = language[::-1]

print('4, reversed string ', reversed_language)

# 5. print a string n times


def repeat(string , n):
    return string * n


print('5. repeat string n times ', repeat('Hi', 5))

# 6. check if a string is a palindrome


def palindrome(string):
    return string == string[::-1]


print('6. check string is palindrome ', palindrome('level'))


# 7. combine a list of strings into a single string
multi_string = ['Dog', 'Cat', 'Panda']

print('7. combine lists into a single string', ''.join(multi_string))

# 8. Find the first element of a list


def head(elements):
    return elements[0]


print('8. return the first ', head([1, 2, 3]))

# 9. Union elements that exists in either of the two lists


def union(list_a, list_b):
    return list(set(list_a + list_b))


print('9. union ', union([1, 2, 3], [2, 3, 5]))

# 10. find all the unique elements presents in a given list


def unique_elements(numbers):
    return list(set(numbers))


print('10. unique elements ', unique_elements([1, 1, 2, 7]))


# 11. find the avg of a list of numbers

def average(*args):
    return sum(args, 0.0) / len(args)


print('11. avg of a list of numbers ', average(1, 5, 7))


# 12. check if a list contains all unique values

def unique(list):
    if len(list) == len(set(list)):
        print('all elements are unique')
    else:
        print('list has duplicate')


print('12. list is all unique values')
unique([1, 2, 3, 4, 4])


# 13. Track frequency of elements in a list

list = [1, 2, 2, 3, 4, 5, 8, 8]

count = Counter(list)

print('13. frequency of a list', count)

# 14. the most frequent element in a list


def most_frequent(list):
    return max(set(list), key=list.count)


numbers = [1, 2, 2, 3, 4, 5, 8, 8]

print('14. find the most frequent element of a list', most_frequent(numbers))


# 15. convert an angle from degrees to radians


def degrees_to_radians(deg):
    return deg * math.pi / 180


print('15. degrees to radians ', degrees_to_radians(90))