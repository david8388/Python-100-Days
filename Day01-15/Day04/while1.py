import random

answer = random.randint(1, 100)
counter = 0

while True:
    counter += 1
    number = int(input('請輸入： '))
    if number > answer:
        print('小一點')
    elif number < answer:
        print('大一點')
    else:
        print('恭喜猜對了！')
        break
print('共猜了%d次' % (counter))

if counter > 7:
    print('需要再加油囉')