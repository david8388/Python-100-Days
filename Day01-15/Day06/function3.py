from random import randint

def roll_dice(num=2):
    total = 0
    for _ in range(num):
        total += randint(1, 6)
    return total

def add(x=0, y=0, z=0):
    return x + y + z

def add2(*args):
    total = 0
    for val in args:
        total += val
    return total

print(roll_dice())
print(roll_dice(2))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

print(add(z = 100, y = 23, x = 1))

print('Call add2')

print(add2())
print(add2(1))
print(add2(1,3))
print(add2(1,3,5))
print(add2(1,3,5,7,9))
