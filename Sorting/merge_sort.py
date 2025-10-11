"""
Merge sort is the most efficient and one of the stable sorting algorithms. It has O(nlogn) time complexity in all cases. 
This follows the divide and conquer paradigm. We repeatdly halves the array into two halves untill the base case of single element array is reached and then combined the sorted arrays.
It uses O(logn) extra space in best case and O(n) in worst case.

"""
nums=[7,1,3,9,35,24,525,51,421,0]

def merge(left, right):
    result=[]
    i=0
    j=0
    
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            

    result.extend(left[i:])
    result.extend(right[j:])
    return result
    

def merge_sort(nums):
    low=0
    high=len(nums)
    mid=(low+high) // 2
    
    left_array = nums[low:mid]
    right_array = nums[mid:high]
    
    if len(left_array)<=1 and len(right_array)<=1:
        return merge(left_array, right_array)
    return merge(merge_sort(left_array),merge_sort(right_array))

print(merge_sort(nums))
        
        