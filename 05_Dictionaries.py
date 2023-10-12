# In dictionary key value pairs are taken
marks = {'Hindi': 80,
         'English': 90,
         'Maths': 84}
print(type(marks))
print(marks['English'])

# .get() method is used to prevent from errors when the key value pair is not present
# print(marks['History'])
print(marks.get('History'))

# Adding items to dictionary of updating the value
marks['Maths'] = 76
print(marks.get('Maths'))

# Deleting values from dictionary
del marks['English']
print(marks)
