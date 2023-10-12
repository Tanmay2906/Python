
# writing in a file

#with open('user_info.txt', 'a') as file:
#    file.write('This is first python file\n')

try:
    with open('user_inf.txt', 'r') as file:
        content = file.readlines()
except Exception as e:
    print(e, type(e))
else:
    print(content)
finally:
    print('DB Closed')