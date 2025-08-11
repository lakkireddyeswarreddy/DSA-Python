
import time

nums = [9, 27, 8, 35, 87, 1]

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time-start_time:.4f} for excution")
        return result
    return wrapper

@execution_time
def max_number(nums):
    maximum = nums[0]
    for i in range(1,len(nums)):
        if nums[i]>maximum:
            maximum=nums[i]
    return maximum

# print(max_number(nums))

random_string = "bbasddubberfbuuuusdcgiwiibdcjewb"

def count_characters(random_string):
    count_dict = dict()
    for char in random_string:
        if char in count_dict:
            count_dict[char]+=1
            continue
        count_dict[char]=1
    return count_dict

# print(count_characters(random_string))\
    
"""
0 is neither positive nor negative, nut factorial of zero is considered as 1 for conventions.
It makes formula like n! = n * (n-1)! work even when n is 1.
"""
    
def factorial(num):
    if num in {0,1}:
        return num
    return num * factorial(num-1)

# print(factorial(int(input("Enter any positive number : "))))
    

