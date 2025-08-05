
nums = [1, 54, 6, 2, 9]

nums1 = [3, 8, 4]


"""
In the list the elements are stored in the continuous memory locations and the list object holds the reference to the memory location of the first element,
so if you access by index i, it will return the value at the list object reference + i
time complexity is O(1)
"""
print(nums[2])

"""
The list object maintains a variable that keeps track of the count of the elements, so when you call the len() method it will simply return the value of the variable.
The time complexity is O(1)
"""
print(len(nums))


"""
Python uses the timsort which is an hybrid of insertion and merge sort, it takes O(nlogn) in worst case and O(n) in best case
and it takes O(n) space in worst and O(1) in best
"""
nums.sort()

"""
This method uses the in-place swaping, it tries to swap the first with the last and the second last with the second first and so on..
It takes O(n/2) == O(n) for reversing
"""
nums.reverse()


"""
Creates a new list and takes O(len(nums)+len(nums1)) time, it returns a new list
it should only accepts a list as a right hand operand
"""
result = nums + nums1

"""
Adds the elements in place to the extending list, it takes O(len(nums1)) time, 
it can extend any iterables like set, tuple, string, dictionary.
eg: nums.extend("abc") creates [1, 54, 6, 2, 9, "a", "b", "c"]
"""

nums.extend(nums1)

"""
Clear method has O(n) time complexity, it needs to go through every element and decrement the refrence count of the element object by one.
if the reference count becomes zero, it will be eligible for the garbage allocation.
"""
nums.clear()  # from python3.3 earlier del nums[:]
print(nums)