def search( nums: list[int], target: int) -> int:
    left=0
    right=len(nums)-1

    while left<=right:
        mid=left+(right-left)//2
        print(nums[mid])
        if nums[mid]==target:
            return mid
        
        if nums[mid]<nums[right]:
            if nums[mid]<target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
        else:
            if nums[left]<=target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        
    return -1

nums=[3,5,1]

print(search(nums,3))
    
    