
"""
Dictionaries are unordered but preserve insertion order from python3.7
They are mutable

"""

sample_dict = dict(name="eswar", age=23)

"""
Since dictionaries are iterable they have length method
"""
print(len(sample_dict))

sample_dict.get("company") # return none if the key doesn't presents, sample_dict["company"] will raise an invalid key error

sample_dict["company"] = "Glory" # adding or reassigning

"""
dictionaries are implemented using hash table, so the keys must be immutable that hashable
keys should be unique, it doesn't through any error it will overried the previous value
"""

del sample_dict["age"] # doesn't return anything
# sample_dict.pop("age")# returns value

print(sample_dict.keys())
print(sample_dict.values())
print(sample_dict.items())

nums_dict={ i:"*" * i  for i in range(1,6)}
print(nums_dict)

"""
It adds the elements from the nums_dict to the sample_dict, if already the key present then the value will be overwritten with the new one """
sample_dict.update(nums_dict) #inplace

"""
Creates a new dict, and adds the one by one items from the both the dictionary starting from left
"""
final_dict = {**sample_dict, **nums_dict} # dictionary unpacking
final_dict_2 = sample_dict | nums_dict # union operator


sample_dict.clear()


