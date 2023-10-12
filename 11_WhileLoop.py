print('Enter a no to check if that is EVEN or not')

user_input = ""
while user_input != 'q':
    user_input = input('Enter a number or q for Quit: ')
    if user_input.isdigit():
        if int(user_input) % 2 == 0:
            print('Number is EVEN')
        else:
            print("No is ODD")


# break --> to stop the loop
# continue --> to stop current iteration of loop and start next iteration

num = [10, -20, 30, -40, 50, -60, 70, -80]

for n in num:
    if n > 0:
        continue
    print(n)