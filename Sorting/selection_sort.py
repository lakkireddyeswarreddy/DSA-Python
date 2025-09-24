"""
In selection sort we divide the list into two parts sorted part and the unsorted part.
Initially sorted part is empty and the unsorted part is the entire list.
In every pass we move the smallest element from the unsorted part to the end of the sorted part.
After i iterations the first i elements are the smallest elements in the nums list.

It has O(n*2) time complexity in worst, best and average cases. 
"""

def selection_sort(nums:list) -> list:
    for i in range(len(nums)-1):
        min_index=i
        for j in range(i,len(nums)):
            if nums[j]<nums[i]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums

nums=[7,1,3,9,35,24,525,51,421,0]

print(selection_sort(nums))