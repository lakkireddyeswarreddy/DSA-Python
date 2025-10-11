"""
Binary search is an efficient searching algorithm that finds an element in the sorted list. The list must be sorted for a binary search.
It works by repeatedly halving the list that the updated list may contain the target element untill the list narrow downs to one element.
Binary search can be implemented in both Iterative and Recursive Cases.
It has O(1) best case time complexity if the element is at the middle of the given list. O(logn) in worst and average cases as we need to divide the list half every time.
It takes O(logn) space in recursive approach for recursive calls and O(1) in iterative approach.
"""

nums = [1, 6, 9, 54, 98, 101, 567, 897]

def binary_search(nums, target):
    left, right = 0, len(nums)-1
    
    while left<=right:
        mid = left + (right-left) // 2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

print(binary_search(nums,target=101))
        

