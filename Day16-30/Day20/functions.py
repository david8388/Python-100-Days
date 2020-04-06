def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder


def calculate_stuff(x, y):
    q, r = divide(x, y)
    print(q, r)


calculate_stuff(10, 2)