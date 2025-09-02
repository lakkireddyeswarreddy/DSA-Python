

"""
Empty set should be declared with the set(), {}-implies empty dictionary
sets are unordered so it doesn't allow indexing
every iterable object has a len() so set has it.
sets are implemented using hash table.
"""
nums_set = set()
nums_set = {2,7,1,5,6}

"""
When you add an element to the set the hash function calculates ths hash value and if that bucket is empty the value is placed at that hash value index,
if not then probing - the next empty bucket.
"""
nums_set.add(2)
#when you add an element, it will calculate the hash value, if the bucket is empty it will add, else it will the check the element with the existing element in the bucket using ==, if it is same it won't add else it will probe to the next empty bucket and add.
nums_set.add(6)
nums_set.add(5)

nums_set.remove(6)#it raises an key error if the element doesn't find in the sets, so use set.discard(3) - it doesn't raise any errors

"""
Finding an elemnt in the list is O(1) as it is implemented based on the hash table

"""

nums_set.pop()#It will return an arbitary element, it will check the hash table and returns the value in the first non empty bucket.

"""
Sets support mathematical operations between sets like union, intersection, differnce and symmetric differnce
"""

nums_set_2 ={ 87, 874,3434}

print(nums_set | nums_set_2) #elements in any one of the sets

print(nums_set & nums_set_2) # elements in both the sets

print(nums_set - nums_set_2) # elements from the set 1 that are not in set 2

print(nums_set ^ nums_set_2) # elements from both the sets but not in both the sets.

nums_set.clear()
