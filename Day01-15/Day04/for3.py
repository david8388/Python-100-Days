for x in range(1, 10, 1):
    for y in range(1, 10, 1):
        print('%d * %d = %d' % (x, y, x * y), end='\t')
    print()

print()

for x in range(1, 10, 1):
    for y in range(1, 10, 1):
        print('%d * %d = %d' % (y, x, x * y), end='\t')
    print()