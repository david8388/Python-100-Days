num = int(input('x = '))
reversedNumber = 0

while num > 0:
    reversedNumber = reversedNumber * 10 + num % 10
    num //= 10

print(reversedNumber)