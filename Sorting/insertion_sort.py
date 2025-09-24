"""
Insertion sort is a basic sorting algorithm. Here we divide the list into sorted and unsorted part. 
In every iteration we take the first element from the unsorted part and keep it in the correct position in the sorted part.
Initially sorted part is the first element and the unsorted part is the remaining elements.
here we don't swap elements like selection sort, we insert the element at it's correct position.
It has O(n*2) time complexity in worst and average case and O(n) in best case.
"""

def insertion_sort(nums:list) -> list:
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while nums[j] > key and j>=0:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums

nums=[7,1,3,9,35,24,525,51,421,0]

print(insertion_sort(nums))