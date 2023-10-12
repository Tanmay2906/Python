# How to define a List
users = ['raju', 'sham', 'Alex']
# Printing complete list
print(users)
# How to get value from List
print(users[0])
print(users[1])

# Appending user with
users.append('Paul')
print(users)

# deleting a value from List
users.remove('raju')
print(users)

# Modifying a value from List
users[0] = "Sham"
print(users)

# Adding items to a list at given position
users.insert(1,'Shanu')
print(users)

# deleting values from a list using index number
del users[2]
print(users)

# Length of List
print(len(users))

# Sorting of List Items
users.sort()
print(users)

# Reverse Sort
users.sort(reverse=True)
print(users)

# Popping the items in List
users.pop()
print(users)

users.append('Paul')
users.append('Aman')
users.append('Bhanu')
# Slicing the List
print(users[0:2])
print(users[2:4])
print(users[-2:])

# Numeric Lists
sell = [2, 9, 13, 28, 35, 4, 56]

# Getting min or max
print(min(sell))
print(max(sell))

# Getting sum of items
print(sum(sell))