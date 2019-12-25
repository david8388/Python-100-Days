x = 5
y = 5

for x in range(1, 6, 1):
    for y in range(1, x + 1, 1):
        print('*', end = '') # end = ''不換行
    print()

print()

for x in range(1, 6, 1):
    for y in range(1, 6, 1):
        if y < 6 - x:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()
