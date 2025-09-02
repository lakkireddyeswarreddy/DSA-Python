

"""
This is an code for reversing an list in place, for reversing using another list just append from the last element.
"""
nums = [4, 7, 9, 20, 48, 3974, 3946, 3, 484]

print(f"list before reversing is : {nums}")

for i in range(len(nums)//2):
    nums[i],nums[-i-1]=nums[-i-1],nums[i]
    
print(f"list after reversing in place is : {nums}")