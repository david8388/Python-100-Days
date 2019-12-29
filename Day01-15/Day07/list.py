list = [1, 3, 5, 7, 100]
print(list)

list2 = ['hello'] * 3
print(list2)

print(len(list), len(list2))

print(list[0])
print(list[4])

# print(list[5]) Caused error because list length just got 4
print(list[-1])
print(list[-3])
list[2] = 300
print(list)

for index in range(len(list)):
    print(list[index])

for elem in list:
    print(elem)

for index, elem in enumerate(list): # Using enumerate will get element and index.
    print(index, elem)