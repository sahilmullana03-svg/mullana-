# 3. what is lambda function in python?
## lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. It is used to create small, throwaway functions without having to give them a name.


# uses of lambda function in python?
## 1. Used with functions like map(), filter(), and reduce()
## 2. Used to create simple, one-line functions
## 3. Used in functional programming paradigms


# add two numbers using lambda function
add = lambda x , y : x+y
print(add(10,20))  ## this is function to add two numbers using lambda function


# cube two numbers 
cube = lambda x: x*x*x 
print(cube(6))  ## this is function to cube a number using lambda function



# lambda with map function.
numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x : x*x, numbers))
print(square)  ## this is function to square a list of numbers using lambda function with map function



#lambda with filter function.
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  ## this is function to filter even numbers using lambda function with filter function


# lambda with reduce function.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  ## this is function to sum a list of numbers using lambda function with reduce function


# lambda with sort function.
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(key=lambda x: x)
print(numbers)  ## this is function to sort a list of numbers using lambda function with sort function


# lambda with sorted function.
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, key=lambda x: x)    

# lambda with sorted function to sort a list of numbers using lambda function with sorted function
print(sorted_numbers)  ## this is function to sort a list of numbers using lambda function with sorted function 


# lambda function with list comprehension.
numbers = [1, 2, 3, 4, 5]   
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  ## this is function to square a list of numbers using lambda function with list comprehension


# lambda functio with user se input lena wala function.
num = int(input("Enter a number: "))
square = (lambda x: x*x)(num)
print(square)  ## this is function to square a number using lambda function with user input

