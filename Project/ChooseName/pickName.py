import numpy as np

with open('name.txt') as f:
    nameList = f.read().splitlines()

randomNames = np.random.choice(nameList, 50, replace=False)

print(randomNames)
