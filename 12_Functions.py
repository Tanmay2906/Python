# Block which perform some task and run it is called
# can be reuse many times in our program which lessen our lines of code
# We can pass arguments to the method

'''
Defining a Function

def myfun():
   print("Function is called)

Calling a Function
myfun()
'''

# Default Arguments
# Dynamic Argument Functions

def greeting(user_name, *hobbies):
    print('*' * 20)
    print(f'Welcome {user_name}')
    for hobby in hobbies:
        print(f'Hobbies is: {hobby}')
    print('Thank you for signing in...')
    print('x' * 20)


greeting('Raju','singing', 'dancing', 'shooting')
greeting('Sham','swimming', 'cooking')
greeting('BabuRao','playing','guitar')


# Dynamic and defaults arguments should be at last than normal one

def greeting2(user_name1,**user_info):
    print('*' * 20)
    print(f'Welcome {user_name1}')
    for key, value in user_info.items():
        print(f'{key} is {value}')
    print('Thank you for signing in...')
    print('x' * 20)


greeting2('Raju', age=18, city='Delhi', email='raju@gmail.com')
greeting2('Sham', age=30, city='Bhopal')
greeting2('baburao',age=40)

