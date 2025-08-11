
#Python built in functions : 

"""
Sum() - it takes two arguments, first the iterable containing integers or float values and then the start value, and the default value of the start is 0.

"""

nums = [i for i in range(5)]

# print(sum(nums, start=10))

# nums = [7, 892, 45634, 21, 34, 4]
nums=[]

# print(min(nums, default="The list is empty")) # the default keyword argument is exists only when we pass the iterable as the first argument.

names = ["eswar", "lakki", "abhi"]
# print(max(names, key=len)) # key is the comparsion function, by default it compares with the value.

"""
map() takes a function as the first argumnet followed by the iterables, we can have any number of iterables, the function arguments count must match with the number of iterables we have passedd.

It returns an iterator,
It is lazily evaluated.
"""

squares_iterator = map(lambda x: x**2, [i for i in range(1,6)])
for square in squares_iterator:
    # print(square)
    pass
# print(list(squares_iterator))

coordinates_iterator = map(lambda x,y : (x,y), [i for i in range(1,6)], [i for i in range(6,11)] )
# print(list(coordinates_iterator))


"""
filter() takes 2 arguments, first the function and the list of the iterables.
it filters the iterable by applying the function on the each item in the iterable if the function returns true it adds the item into the return iterator object.
It returns the iterator and it is lazily evaluated.

"""

even_iterator = filter(lambda x: x%2==0,[i for i in range(1,10)])
# print(list(even_iterator))

"""
reduce() comes from the functools package from the python 3,
it takes three argumnets, first the function with 2 arguments(accumulator, item), second the iterable, third the optional initial value of the accumulator.
It returns the single value
iT is used for reducing the iterable into a single value
"""
from functools import reduce

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
        
eswar = Student("eswar", 23)
abhi = Student("abhi", 25)

max_age_student = reduce(lambda x,y: x if x.age > y.age else y, [eswar, abhi])

# print(max_age_student)


"""
Function is a block of code that can perform a partcular task.
Functions support reusability and modularity.
We have regular functions that has name defined with def keyowrd and ananymous function that doesn't have named defined with lambda
Regular functions can have multiple expressions, but lambda functions can only have one expressions but can use conditional expressions.
Regular functions may or may not have return value, lambda functions automatically returns the expression value after computation.
regular functions have docstring which defines what the function does, lambda function doesn't have docstring.
"""

# def is_even(num):
#     """calculates whether the num is even or not"""
#     return True if num%2 ==0 else False
# print(is_even(5))
# print(is_even.__doc__)

is_even = lambda x : x % 2 == 0
# print(is_even(6))

"""
parameters are the variables that are used in the function definition.
arguments are the values passed to the function call.

We have three types of arguments.
1. positional - order as same as the parameters.
2. keyword - passing arguments along with the parameter name.
3. default - optional argument, the value is given at the function definition itself.
"""

# def sum(a,b=10):
#     return a+b
# print(sum(2,3)) # postional 
# print(sum(b=3,a=2)) # keyword
# print(sum(a=5)) # default

"""
If you don't know the number of positional and keyword arguments at the function definition you can use 
1. *args for positional, which returns the positional arguments as a tuple
2. **kwargs for keyword, which returns the keyword arguments as a dict
"""

# def example(*args, **kwargs):
#     print(f"positonal arguments :{args}")
#     print(f"keyword arguments :{kwargs}")
    
# example(1,8,6,75,9, name="eswar", age=23)

"""
Closure is a function that has access to the outerscope function variables, even after the outer function scope has completed.
Closures are useful for encapsulation without classes.
Closures are used to maintain state across the function invocations without the global variables.etc.
"""

"""
Decorators are functions that take argument as other functions and adds or alter the behaviour of the function without explicitly modifing the source code of the function.
Decorators are used for logging.
Decorators are used for authentication.
Decorators are used for caching, preprocessing data, retry logic, performance measures etc.
"""
    