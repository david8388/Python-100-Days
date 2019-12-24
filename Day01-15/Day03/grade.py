score = int(input('請輸入分數： '))

if score >= 90:
    grade = 'A'
elif score >= 80 and score < 90:
    grade = 'B'
elif score >= 70 and score < 80:
    grade = 'C'
elif score >= 60 and score < 70:
    grade = 'D'
else:
    grade = 'E'

print('等級為：', grade)

