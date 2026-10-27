## 1. user defined function
## user-defined functions are functions that are defined by the user to perform a specific task.    

def add(a, b):
    """
    This function adds two numbers.
    """

    
    print(a+b)

add(10, 20)  ## this is function to add two numbers
print(add.__doc__)  ## this is function to print docstring of add function

def print_values():
    """
    This function prints some values.
    """
    print("Hello, World!")
    print("This is a function to print values.")

print_values()  ## this is function to print values.
print(print_values.__doc__)  ## this is function to print docstring of print_values function



##function with parameters
def multiply(a, b):
    """
    This function multiplies two numbers.
    """
    print(a*b)

multiply(10,20)  ## this is function to multiply two numbers
print(multiply.__doc__)  ## this is function to print docstring of multiply function


## function with return value 
def divide(a,b):
    """
    This function divides two numbers.
    """
    return a/b
print(divide(10,2))  ## this is function to divide two numbers
print(divide.__doc__)  ## this is function to print docstring of divide function


# what is docstring in python
## docstring is a string that is used to document a function, class or module.
