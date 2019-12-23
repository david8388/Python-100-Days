import math

radius = float(input('請輸入半徑： '))
perimeter = radius * 2 * math.pi
area = radius* radius * math.pi

print('半徑為：%.2f' % ( radius ))
print('圓周長為：%.2f' % ( perimeter ))
print('面積為：%.2f' % ( area ))