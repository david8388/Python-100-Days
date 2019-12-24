
value = float(input('請輸入長度： '))
unit = input('請輸入單位： ')

if unit == 'in' or unit == '英吋':
    print('%.2f英吋 = %.2f公分' % (value, value * 2.54))
elif unit == 'cm' or unit == '公分':
    print('%.2f公分 = %.2f英吋' % (value, value / 2.54))
else:
    print('請輸入有效單位')