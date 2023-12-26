#1. Function defination is one time process
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

#2. Fuction calling/invoking is many time process
greet('Pranav', 'Sourav', 'Ujjwal')