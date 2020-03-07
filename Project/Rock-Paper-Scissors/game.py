import random

rock_paper_scissors = ['rock', 'paper', 'scissors']

computer = random.choice(rock_paper_scissors)

while True:
    user = input('Please enter the value(rock, paper, scissors) ')
    if user not in rock_paper_scissors:
        print('Input Error! Please enter the value(rock, paper, scissors) ')
    else:
        if computer == user:
            print('Draw')
        elif computer == 'rock':
            if user == 'paper':
                print('User wins')
            else:
                print('computer wins')
        elif computer == 'paper':
            if user == 'scissors':
                print('User wins')
            else:
                print('computer wins')
        elif computer == 'scissors':
            if user == 'rock':
                print('User wins')
            else:
                print('computer wins')
        print('computer is {}'.format(computer))
        print('user is {}'.format(user))
        break

