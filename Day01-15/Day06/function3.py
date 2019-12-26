from random import randint

def roll_dice(num=2):
    total = 0
    for i in range(num):
        total += randint(1, 6)
    return total

def add(x=0, y=0, z=0):
    return x + y + z

print(roll_dice())
print(roll_dice(2))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

print(add(z = 100, y = 23, x = 1))