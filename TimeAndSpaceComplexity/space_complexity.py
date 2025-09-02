

"""
Space complexity is also a way to measure the efficieny of an algorithm, it express the growth rate of memory space required by the algorithm for its completion as the input size increases.

Every algorithm has fixed size elements and variable size elements and the auxilary space.

1. Fixed size elements are the constants or the fixed size variables, and the programm instructions.

2. Variable size elements are the input size elements

3. Auxilary space is the temporary space required by an algorithm for it's execution like temporary data structures, temporary variables and the recursion call stack.

space complexity = fixed + variable + auxilary space.

"""


def factorial(n): 
    # if n<=1:
    #     return 1
    # return n * factorial(n-1)
    total = 1 # fixed size variable
    for i in range(2,n+1): # fixed size i variable
        total*=i
    return total

"""
It requires only constant space for storing the value of n, and it doesn't grow with the value of n, so there is no change in the input memory space.
Auxilary space complexity is O(n), as there are n recursion calls in the call stack, as it takes n calls to reach the base case.
so, space complexity is O(n)
"""

# print(factorial(5))


def add_numbers_to_list(n):
    nums = [] # variable size data structure, it grows with the input size linearly
    for i in range(n): #fixed size i variable
        nums.append(i)
    return nums 

# print(add_numbers_to_list(10)) # space complexity is O(n) as the space increases with the input size.


def no_of_ways(n):
    a=1
    b=2
    for i in range(3,n+1): # space complexity is O(1) as we are using only constant space for a and b, time complexity is O(n)
        c=a+b
        a=b
        b=c
    return b
    if n<=2:
        return 2
    return no_of_ways(n-1) + no_of_ways(n-2) # auxilary space is O(n) as there are n calls in the call stack, space complexity is O(n), Time complexity is O(2^n) as there are two calls for each number without memoization.


# def no_of_ways(n, ways=None):
#     if ways is None:ways ={}
#     if n in ways:
#         return ways[n]
#     ways[n]= no_of_ways(n-1,ways)+no_of_ways(n-1,ways)