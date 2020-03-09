import random

fruits = ['apple', 'mango', 'grape', 'guava', 'melon']
chances = 7
randomFruit = random.choice(fruits)
starLength = len(randomFruit)
starWord = ''
isSuccess = False

for _ in range(starLength):
    starWord += '*'

print('Guess the word! HINT: word is a name of a fruit')
print(starWord)

for _ in range(chances):
    char = str(input('Enter a letter to guess: '))
    for i in range(starLength):
        if randomFruit.find(char, i):
            print(char, end='')
        else:
            print('*', end='')
        print()
