sum = 0
sum2 = 0
sum3 = 0

for x in range(0, 101, 2):
    sum += x

print('1~100偶數和為', sum)

for x in range(2, 101, 2):
    sum2 += x
print('1~100偶數和為', sum2)

for x in range(101):
    if x % 2 == 0:
        sum3 += x
print('1~100偶數和為', sum3)

