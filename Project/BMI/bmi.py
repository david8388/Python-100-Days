height = int(input('Please input your height(cm): '))
weight = int(input('Please input your weight(kg): '))

bmi = weight / (height / 100) ** 2

print(bmi)

if bmi < 18.5:
    print('Your BMI is underweight')
elif 18.5 <= bmi <= 24:
    print('Your BMI is normal')
else:
    print('Your BMI is overweight')
