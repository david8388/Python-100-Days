import random

number = random.randint(1, 20)

while True:
    guessNumber = int(input('Guess a number '))
    if guessNumber == number:
        print('Congrats!!! The number is ', guessNumber)
        break;
    elif guessNumber >= number:
        print('Number is too high!!')
    else:
        print('Number is too low!!')


