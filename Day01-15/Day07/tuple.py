t = ('David', '25', True, 'Taiwan')
print(t)

print(t[0])
print(t[1])

for member in t:
    print(member)

t = ('LBJ', '35', True, 'Ohio')

print(t)
# tuple to list
person = list(t)
print(person)
person[0] = '小明'
person[1] = 20
print(person)

# list to tuple

fruits = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits)
print(fruits_tuple)