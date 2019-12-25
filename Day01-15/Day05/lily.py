for num in range(100, 1000):
    unitDigit = num % 10
    tensDigit = num // 10 % 10
    hundredsDigit = num // 100
    if num == unitDigit ** 3 + tensDigit ** 3 + hundredsDigit ** 3:
        print('%d為水仙花數' % (num))
