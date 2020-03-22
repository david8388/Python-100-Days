length = int(input('Enter the height of pyramid '))

i = 0

x = length


def asterisk(times):
    return '*' * (1 + (times - 1) * 2)


# triangle
while i < length:
    i += 1
    spaceTimes = length - i
    print(' ' * spaceTimes, asterisk(i))

# Inverted triangle
while x > 0:
    spaceTimes = length - x
    print(' ' * spaceTimes, asterisk(x))
    x -= 1
