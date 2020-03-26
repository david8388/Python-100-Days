import numpy as np
import pandas as pd

with open('name.txt') as f:
    nameList = f.read().splitlines()

randomNames = np.random.choice(nameList, 50, replace=False)

grades = np.random.randint(0, 101, (50, 4))

df = pd.DataFrame(grades)

df.columns = ['國文', '英文', '數學', '自然']

df['姓名'] = randomNames

df = df[['姓名', '國文', '英文', '數學', '自然']]

chinesePass = []
engNotPass = []
mathPassScienceNotPass = []

for row, x in df.iterrows():
    print(x)
    name = x['姓名']
    if x['國文'] >= 60:
        chinesePass.append(name)
    if x['英文'] < 60:
        engNotPass.append(name)
    if x['數學'] >= 60 and x['自然'] < 60:
        mathPassScienceNotPass.append(name)

print('Chinese Pass', chinesePass, end='\n')
print('English Not Pass', engNotPass, end='\n')
print('Math Pass but Science Not Pass', mathPassScienceNotPass)

#for key, value in df.iteritems():
#    print('key', key)
#    print('value', value)