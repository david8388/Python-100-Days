length = int(input('Enter the height of pyramid '))

i = 0


def asterisk(times):
    return '*' * (1 + (times - 1) * 2)


while i < length:
    i += 1
    spaceTimes = length - i
    print(' ' * spaceTimes, asterisk(i))
