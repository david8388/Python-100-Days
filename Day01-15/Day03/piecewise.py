x = float(input('x = '))

# first
if x > 1:
    y = 3 * x - 5
elif 1 >= x and x >= -1:
    y = x + 2
else:
    y = 5 * x + 3


# second
if x > 1:
    y2 = 3 * x - 5
else: 
    if x >= -1:
        y2 = x + 2
    else:
        y2 = 5 * x + 3



print('First：f(%.2f) = %.2f' % (x, y))
print('Second：f(%.2f) = %.2f' % (x, y2))