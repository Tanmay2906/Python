import random

while True:
    print(f'Number is {random.randint(1,6)}')
    user_input = input('Do you want to continue y/n:')
    if user_input == 'n':
        break