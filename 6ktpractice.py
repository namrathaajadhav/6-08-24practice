#recursive function 
def factorial(n):
    if n == 0 or n== 1:
        return 1
    else:
        return n* factorial(n-1)
number = 7 #7*6*5*4*3*2*1
result = factorial(number)
print(result)

#lambda function

square = lambda x: x * x
result = square(5)
print(result)


#map()
numbers = [1,2,3,4,5]
def square(x):
    return x * x
square_numbers = map(square, numbers)
print(list(square_numbers))


#filter()
numbers = [1,2,3,4,5,6,7,8]
def is_even(number):
    return number % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers))


#reduce()
from functools import reduce
numbers = [1,2,3,4,5]
def add(a,b):
    return a + b
result = reduce(add, numbers)
print(result)

    
