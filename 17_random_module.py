import random

# Generate a random float between 0 and 1
random_float = random.random()
print(random_float)

# Generate a random integer between two numbers
random_integer = random.randint(1,100)
print(random_integer)

# Generate a random float between two user defined numbers
random_float = random.uniform(3.5, 6.5)
print(random_float)

# Generate a random choice from a list
options = ["apple", "banana", "pineapple", "cherry", "date"]
random_choice = random.choice(options)
print(random_choice)

# Shuffling the Values of List
print(options)
random.shuffle(options)
print(options)