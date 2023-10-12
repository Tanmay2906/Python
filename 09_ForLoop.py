# Execute a block of code for each item in the sequence
# (such as list, tuple, string or range)

for i in 1, 2, 3, 4, 5:
    print(i)

# Using for loop with the list

user_list = ['Alex', 'Ram', 'Baburao', 'Tanmay']
for user in user_list:
    print(user)

# Using for loop with the dictionary

age_info = {'Raju' : 25, 'Sham' : 21}
for name in age_info.keys():
    print(name)
for age in age_info.values():
    print(age)

for name, age in age_info.items():
    print(f'Name: {name}')
    print(f'Age {age}')


# using range in for loop --> print till last value - 1
for num in range(1, 9):
    print(num)