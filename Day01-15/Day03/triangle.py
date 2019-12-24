import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('周長為%.2f' % (a + b + c))
    # 求三角形面積用海龍公式
    s = (a + b + c)/ 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print('面積為%.2f' % (area))
else:
    print('不能構成三角形')