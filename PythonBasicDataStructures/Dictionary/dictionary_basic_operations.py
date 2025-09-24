
"""
Dictionaries are unordered but preserve insertion order from python3.7
They are mutable

"""

sample_dict = dict(name="eswar", age=23)

"""
Since dictionaries are iterable they have length method
"""
print(len(sample_dict))

#Accessing the value of a key is O(1) operation on average as it is implemented using hash table.In Worst case it may take O(n) time if there are many collisions.
sample_dict.get("company") # return none if the key doesn't presents, sample_dict["company"] will raise an invalid key error

#Assigning a value to a key is also O(1) operation on average as it is implemented using hash table.In Worst case it may take O(n) time if there are many collisions.
sample_dict["company"] = "Glory" # adding or reassigning

"""
dictionaries are implemented using hash table, so the keys must be immutable that hashable
keys should be unique, it doesn't through any error it will overried the previous value
"""
#Removing a key has an average time complexity of O(1), in worst case it may take O(n) time if there are many collisions.
del sample_dict["age"] # doesn't return anything
# sample_dict.pop("age")# returns value

print(sample_dict.keys())
print(type(sample_dict.values())) # it will return a dict_values object which is iterable and can be converted to list, set, tuple etc.
print(type(sample_dict.items()))#it will return a dict_items object which is iterable and can be converted to list, set, tuple etc.

for key, value in sample_dict.items():
    print(f"{key} : {value}")
    
for key in sample_dict:
    print(f"{key} : {sample_dict[key]}")
    
for value in sample_dict.values():
    print(value)

nums_dict={ i:"*" * i  for i in range(1,6)}
print(nums_dict)

"""
It adds the elements from the nums_dict to the sample_dict, if already the key present then the value will be overwritten with the new one """
sample_dict.update(nums_dict) #inplace

"""
Creates a new dict, and adds the one by one items from the both the dictionary starting from left
"""
#Both are same and can unpack or use union operator for more than two dictionaries.
# for inplace merging use |= operator or update() method.
#Both method has the O(n) time complexity as it needs to go through each elements and add to the hash table.Where n is the total number of elements in both the dictionaries.
final_dict = {**sample_dict, **nums_dict} # dictionary unpacking
final_dict_2 = sample_dict | nums_dict # union operator

#Clear the dictionary has O(n) time complexity as it needs to go through each elements and removed the value from the hash table.
sample_dict.clear()


