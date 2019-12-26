def factorial(num):
    result = 1
    for num in range(1, num + 1):
        result *= num
    return result

m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))
