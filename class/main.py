# main.py
# Importing a function from the module we wrote

from module import extract_first_name
full_name = input("Enter your full name: ")
first_name = extract_first_name(full_name)
greeting = "Hello " + first_name + "!"
print(greeting)