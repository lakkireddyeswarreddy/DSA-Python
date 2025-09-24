"""
Bubble sort is a basic sorting algorithm, it repeatedly swaps the adjacent elements if they are in the wrong order. In every pass the largest element will bubble upto the end of the list.
It has O(n*2) time complexity in worst and average cases and O(n) in best case.
It has O(1) space complexity as we are swapping the elements in-place.
We perform maximum of n-1 passes.

"""
def bubble_sort(nums:list) -> list:
    
    for i in range(len(nums)-1):
        is_swapped=False
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swapped=True
        if not is_swapped:
            break
    return nums

nums=[7,1,3,9,35,24,525,51,421,0]

print(bubble_sort(nums))
    