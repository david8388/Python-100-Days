fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']

fruits2 = fruits[1:4]
print(fruits2)
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-3: -1]
print(fruits4)
fruits5 = fruits[::-1]
print(fruits5)

list = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list)
list3 = sorted(list, reverse = True)
list4 = sorted(list, key = len)
print(list2)
print(list3)
print(list4)

list.sort(reverse = True)
print(list)