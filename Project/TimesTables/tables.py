
for i in range(2, 10):
    for x in range(1, 10):
        print('{} * {} = {}'.format(i, x, i * x))

print('------------------------')

for x in range(1, 10):
    for i in range(2, 10):
        print('{} * {} = {:2}  '.format(i, x, i * x), end='')
    print()

