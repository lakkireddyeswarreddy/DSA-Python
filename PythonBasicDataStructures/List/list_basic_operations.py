
nums = [1, 54, 6, 2, 9]

nums1 = [3, 8, 4]

nums1.remove(3) # by value, it raises a value error if the value is not found in the list. It removes the first occurence of the value.It doesn't return anything.
nums1.pop() # by index, it raises an index error if the index is out of range, if no index is provided it removes the last element. It returns the removed element.
del nums1[0] # by index, it raises an index error if the index is out of range. It doesn't return anything.
nums = [x for x in nums if x!=2] # removes all the occurences of the value, it creates a new list and assigns to the variable.
nums[:] = [x for x in nums if x!=2] # removes all the occurences of the value, it modifies the existing list in place.

del nums[:: 3] # removes every 3rd element from the list, it modifies the existing list in place.
#here the step value is 3, so it starts from index 0 and removes every 3rd element.

#acessing an element in the list by index is an constant time operation.As the list object holds the reference to the memory location of the first element in the list.

nums.index(8) # returns the index of the first occurence of the value, raises a value error if the value is not found in the list.


"""
In the list the elements are stored in the continuous memory locations and the list object holds the reference to the memory location of the first element,
so if you access by index i, it will return the value at the list object reference + i
time complexity is O(1)
"""
print(f"2nd index element in the nums list is : {nums[2]}")

"""
The list object maintains a variable that keeps track of the count of the elements, so when you call the len() method it will simply return the value of the variable.
The time complexity is O(1)
"""
print(f"Elements count in the nums list : {len(nums)}")


"""
Python uses the timsort which is an hybrid of insertion and merge sort, it takes O(nlogn) in worst case and O(n) in best case
and it takes O(n) space in worst and O(1) in best
"""
nums.sort()
print(f"Sorted list is {nums}")

"""
This method uses the in-place swaping, it tries to swap the first with the last and the second last with the second first and so on..
It takes O(n/2) == O(n) for reversing
"""
nums.reverse()
print(f"Reverse sorted list is {nums} ")

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

nums.extend(nums1) # with dictionary it will only add the keys to the list.

print(f"Extended nums list is : {nums}")

"""
Clear method has O(n) time complexity, it needs to go through every element and decrement the refrence count of the element object by one.
if the reference count becomes zero, it will be eligible for the garbage allocation.
"""
nums.clear()  # from python3.3 earlier del nums[:]