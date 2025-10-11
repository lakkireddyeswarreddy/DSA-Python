"""
Quick sort is an advanced sorting algorithm. It is efficient compared to basic sorting algorithms.
It has O(nlogn) time complexity in best and average cases, and O(n*2) in worst case.
In quick sort we select a pivot element and then move all the elements less than the pivot to the left and greater than pivot to the right.
It follows the divide and conquer paradigm, where base case the single element array.

The key step in quick sort is partitioning. 
We have three different partitioning in quick sort :

1. Naive partition : Most simple and stable approach.
This is not the in-place, we use O(n) extra space  for sorting. 
In this we create three arrays left, middle and right. left for the elements that are less than the pivot, middle for the elements equal to pivot, and right for the elements greater.
and then we recursively sort the left and right parts.
This is not used in the production.

2.Lomuto partition : This is most efficient approach.
Here we select the last element as the pivot, and initialize the two variables from -1 and 0 indexes. If the value is greater than the pivot we move, if value is less we swap with the low index.
It is in-place.

3.Hoare partition : This is unstable and efficient algorithm.
Here we select the first element as the pivot, and initialize two variables left and right, we move left untill we find an element greater than pivot and right untill we find element less than pivot and then swap them.
We will stop if left>right.

"""

nums=[7,1,3,9,35,24,525,51,421,0]

#Naive partition.

def partition(nums, pivot):
    left=list()
    middle=list()
    right=list()
    for num in nums:
        if num<pivot:
            left.append(num)
        elif num>pivot:
            right.append(num)
        else:
            middle.append(num)
            
    return left, middle, right

def quick_sort(nums):
    
    if len(nums)<=1:
        return nums
    
    pivot = nums[len(nums)-1]
    left, middle, right = partition(nums,pivot)
    
    return quick_sort(left) + middle + quick_sort(right)


#Lomuto partition

def partition_lomuto(nums,starting_index, pivot_index):
    
    i=starting_index-1
    for j in range(starting_index,pivot_index):
        if nums[j] < nums[pivot_index]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
    i+=1
    nums[i],nums[pivot_index]=nums[pivot_index],nums[i]
    return i

def quick_sort_lomuto(nums, left,right):
    if len(nums)<=1:
        return
    if left<right:
    
        pivot_index=right-1
        
        returned_index = partition_lomuto(nums,left, pivot_index)
        quick_sort_lomuto(nums,left,returned_index)
        quick_sort_lomuto(nums,returned_index+1,right)
        
    return nums
        

# print(quick_sort_lomuto(nums,0,len(nums)))

#Hoare partition

def partition_hoare(nums, left, right):
    pivot=nums[left]
    i=left
    j=right
    
    while True:
        
        while nums[i]<pivot:
            i+=1
            
        while nums[j]>pivot:
            j-=1
            
        if i>=j:
            return j
        
        nums[i],nums[j]=nums[j],nums[i]
    

def quick_sort_hoare(nums, left, right):
    
    if len(nums)<=1:
        return nums
    
    if left<right:
        returned_index=partition_hoare(nums,left,right)
        quick_sort_hoare(nums,left,returned_index)
        quick_sort_hoare(nums,returned_index+1,right)
        
    return nums

print(quick_sort_hoare(nums, 0, len(nums)-1))
        