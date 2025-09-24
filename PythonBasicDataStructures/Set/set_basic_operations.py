

"""
Empty set should be declared with the set(), {}-implies empty dictionary
sets are unordered so it doesn't allow indexing
every iterable object has a len() so does the set.
sets are implemented using hash table.
"""
#Sets are implemented using hash table, so the elements must be immutable that hashable.

nums_set = set()
nums_set = {2,7,1,5,6}

"""
When you add an element to the set the hash function calculates ths hash value and if that bucket is empty the value is placed at that hash value index,
if not then probing - the next empty bucket.
"""
#Adding the element has a average time complexity of O(1), in worst case it may take O(n) time if there are many collisions.
nums_set.add(2)
#when you add an element, it will calculate the hash value, if the bucket is empty it will add, else it will the check the element with the existing element in the bucket using ==, if it is same it won't add else it will probe to the next empty bucket and add.
nums_set.add(6)
nums_set.add(5)

#Removing an element has an average time complexity of O(1), in worst case it may take O(n) time if there are many collisions.
nums_set.remove(6)#it raises an key error if the element doesn't find in the sets, so use set.discard(3) - it doesn't raise any errors

"""
Finding an elemnt in the set is O(1) as it is implemented based on the hash table

"""

nums_set.pop()#It will return an arbitary element, it will check the hash table and returns the value in the first non empty bucket.
#As the set is unordered it doesn't support indexing
# print(nums_set[0]) # it raises an type error

"""
Sets support mathematical operations between sets like union, intersection, differnce and symmetric differnce
"""

nums_set_2 ={ 87, 874,3434}

print(nums_set | nums_set_2) #elements in any one of the sets

print(nums_set & nums_set_2) # elements in both the sets

print(nums_set - nums_set_2) # elements from the set 1 that are not in set 2

print(nums_set ^ nums_set_2) # elements from both the sets but not in combined.

nums_set.clear()
# It has the linear time complexity as it needs to go through each elements and removed the value from the hash table.
print(nums_set)
