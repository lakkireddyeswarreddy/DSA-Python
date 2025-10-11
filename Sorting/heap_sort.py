"""
Heap sort is an advanced and efficient sorting algorithms. It use the comparative approach.
It is implemented using the complete binary tree called heap.
A heap is a complete binary tree that has heap properties.
Heap sort is implemented using the max-heap.
First we heapify the given array from the first non-leaf node. We can get the first non-leaf node from (n//2 -1), where n is the length of the array.
and then we heapify the nodes untill to the root code.
A root node  is said to be sorted if the value at index 2*i +1 and 2*i +2 are less than the value at index i.
After heapifying the array, we swap the root node with the last element and reduce the size of the heap by 1.
and then we heapify the root node.
It has O(nlogn) time complexity in all cases and is in-place.
Due to stability merge sort is prefered over the heap sort.
"""


nums=[7,1,3,9,35,24,525,51,421,0]

def heapify(array, n, i):
    while True:
        root_index = i
        left = 2*i + 1
        right = 2*i + 2
        
        if left<n and array[left]>array[root_index]:
            root_index=left
            
        if right<n and array[right]>array[root_index]:
            root_index=right
            
        if root_index!=i:
            array[i],array[root_index]=array[root_index],array[i]
        else:
            break
        i=root_index
    

def heap_sort(nums):
    
    for i in range(len(nums)//2-1, -1,-1):
        heapify(nums,len(nums),i)
        
    print(nums)
        
    for j in range(len(nums)-1, 0,-1):
        nums[0],nums[j]=nums[j],nums[0]
        heapify(nums,j,0)
        
    return nums
        
print(heap_sort(nums))