num = int(input('請輸入數字： '))
end = int(num / 2)
isPrime = True

for x in range(2, end + 1):
    if num % x == 0:
        isPrime = False
        break

if isPrime == True and num != 1:
    print('%d為質數' % (num))
else:
    print('%d不是質數' % (num))