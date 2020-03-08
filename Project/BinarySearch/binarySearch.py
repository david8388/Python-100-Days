import random

randomList = []

user = int(input('Please enter the even value you want to search '))

# create even array
for i in range(0, 100, 2):
    randomList.append(i)

def binary_search(start, end, hkey):
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if randomList[mid] > hkey:
        return binary_search(0, mid - 1, hkey)
    elif randomList[mid] < hkey:
        return binary_search(mid + 1, end, hkey)
    return mid


result = binary_search(0, len(randomList), user)

if result != -1:
    print('Element is at index %d' % result)
else:
    print('Element is not present in array')
