# https://www.idomaths.com/zh-Hant/hcflcm.php#divprime
# 取最大公因數GCD 及最小公倍數 LCM

x = int(input('x = '))
y = int(input('y = '))

if x > y:
    x, y = y, x

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d及%d的最大公因數為%d' % (x, y, factor))
        print('%d及%d的最小公倍數為%d' % (x, y, x * y / factor))
        break