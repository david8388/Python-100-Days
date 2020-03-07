import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

numberOfPassword =  int(input('Number of password? '))
length = int(input('Password length? '))

for n in range(numberOfPassword):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)