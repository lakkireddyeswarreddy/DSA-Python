
"""
range doesn't take any keyword arguments, here the first positional argument is the start, and followed by the end and at the end the step
"""
# for i in range(1, 10, 1):
#     if i%2==0:
#         continue
#     # if i==9:
#     #     break
#     print(i)
    
# else:
#     print("loop completed without breaking") # this block of code will only excuted when the loop is completed without any breaks, skipping the iteration is allowed using continue.
    
    
"""
In the while loop you need to manually update the condition checking variable but in the for loop it will automatically increase based on the step we mentioned, the default value for step is 1.
"""
    
# """
# uisng while loop with the true is not a good idea, avoid this.
# """

# while True:
#     print("I am from the while loop")

# i=0
# while i<20:
#     print(i)
#     i+=1


"""
Iteration tools used with for loop :

1. range() - it is used to generate sequential numbers, it takes atmost three arguments, first the start number of the sequence, second the last + 1 number, end the differnce between the each number.

2. enumerate() - it is used to get both the index and value from an iterable.

3. zip() -  it is used for iterating multiple iterables parallely.

4. reversed() - it used to reverse the members of the iterables and iterate over them.

5. sorted() - sorts the iterable members and then iterates over them.
"""

# for i in range(1,11,2):
#     print(i)
    
names = ["eswar", "lakki", "abhi"]

ages = [23, 21, 25]

# for i, name in enumerate(names):
#     print(f"{i+1} - {name}")
    
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old.")
    
# for age in sorted(ages):
#     print(age)
    
# for name in reversed(names):
#     print(name)


# for index, (name, age) in enumerate(zip(names, ages)): # zip function returns an iterable zip object which returns the tuple when iterated over, and the zip object is lazily evaluated
#     """
#     When iterating over multiple iterables of unequal length using zip, the zip functions stops when the shortest iterable is exhausted.
#     Zip object can be converted to list, dict, tuple etc. if needed.
#     """
#     print(f" {index+1} -{name} is {age} years old.")

#Use list comprehensions whenever possible they are faster than the normal loops.
# even_numbers = [num for num in range(10) if num%2==0]
# print(even_numbers)

"""
generator expressions are similar to the list comprehensions, use parenthensis for generator expressions instead of square brackets.

List comprehensions return entire list numbers, bu the generator expression returns a generator object, which is lazily evaluated and yields the each member when iterated over.

generator objects can be iterated only once.

"""

# even_generator = (num for num in range(10) if num%2==0)
# for num in even_generator:
#     print(num)
# for num in even_generator:
#     print(num)


"""
Nested loops using list comprehensions and generator expressions.
"""

list_cooridnates = [(i,j) for i in range(5) for j in range(6)]
print(list_cooridnates)
    
coordinates = ((i,j) for i in range(1,4) for j in range(1,4))
for cooridnate in coordinates:
    print(cooridnate)