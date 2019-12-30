list = [1, 3, 5, 7, 100]

list.append(200)
list.insert(1, 400)

print(list)

list += [1000, 2000]

print(list)
print(len(list))

if 3 in list:
    list.remove(3)
if 1234 in list:
    list.remove(1234)

print(list)

list.pop(0)
print(list)
list.pop(len(list) - 1)
print(list)

list.clear()
print(list)