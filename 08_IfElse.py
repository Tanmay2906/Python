
if 10>8:
    print('Hey it is True')
    print('This is if Else')
else:
    print('Hey it is False')

print(10 < 8)


print('Enter a no to check if that is EVEN or not')
num = int(input('Enter a Number: '))

if num % 2 == 0:
    print('Yes Number is EVEN');
else:
    print("No is ODD")

users = ['paul', 'raju', 'sham']
if 'paul' in users:
    print('User Exist')

elist = ['Tanmay']
if elist:
    print('List is not Empty')
else:
    print('List is Empty')

# ELIF
marks = int(input('Enter the marks: '))
if marks >= 80:
    print('1st Division')
elif marks >= 60:
    print('2nd Division')
elif marks >= 40:
    print('3rd Division')
else:
    print('Failed!')

# Nested IF ELSE

age = 20
voter_id = False
if age >= 18:
    if voter_id:
        print('Yes you can vote')
    else:
        print('Apply for Voter Id First')
else:
    print('You Cannot Vote!')

if age >= 18 or voter_id:
    print('You can vote')
else:
    print('You cannot Vote')