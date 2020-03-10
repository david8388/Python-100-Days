import random

fruits = ['apple', 'mango', 'grape', 'guava', 'melon']
randomFruit = random.choice(fruits)
chances = len(randomFruit) + 2
starLength = len(randomFruit)
word = ''
isSuccess = False

for _ in range(starLength):
    word += '*'

print('Guess the word! HINT: word is a name of a fruit')
print(word)

for attempt in range(chances):
    guessWord = str(input('The {0} Try! \nEnter a letter to guess: '.format(attempt+1)))
    for i in range(starLength):
        if guessWord == randomFruit[i]:
            word = word[:i] + guessWord + word[i+1:]
        elif not word[i].isalpha():
            word = word[:i] + '*' + word[i+1:]
        if word == randomFruit:
            isSuccess = True
            break
    if isSuccess:
        print('Congrats!! The word is {0}'.format(word))
        break
    if not isSuccess and attempt == chances - 1:
        print('You lose! The word is {0}'.format(randomFruit))
    else:
        print(word)
