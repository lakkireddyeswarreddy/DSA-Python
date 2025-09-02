
const_nums = 34,5,6


"""
We can declare a tuple with the parenthesis or without but commas are required.
"""
print(f"Type of nums is {type(const_nums)}")

print(f"Count of elements : {len(const_nums)}")

print(f"Index of element 6 is {const_nums.index(6)}")


"""
Tuples are immutable and faster than the lists.
"""
#  Key Reasons Tuples Are Faster Than Lists
# Immutability:

# Tuples are immutable, meaning their contents cannot be changed after creation.
# This allows Python to make certain optimizations during runtime, such as storing them in a more compact and efficient way.
# Memory Efficiency:

# Tuples use less memory than lists because they don’t need to store extra information for dynamic resizing.
# Lists are designed to be mutable and resizable, so they allocate extra memory to accommodate future changes.
# Simpler Operations:

# Since tuples don’t support operations like append(), remove(), or pop(), Python doesn’t need to maintain the overhead for these methods.
# This makes tuple operations like iteration and access faster.
# Caching:

# Python can cache tuples more effectively than lists, especially when they are used as keys in dictionaries or elements in sets.
# Fixed Size:

# The fixed size of tuples allows Python to optimize access patterns and memory layout, which contributes to faster performance.

print(f"Element at the 0th index is :{const_nums[0]}")
"""
Tuples can be used as a key in the dictionary if it has immutable types
"""
print(5 in const_nums) # it is an O(n) operation as it needs to check each element in the tuple.