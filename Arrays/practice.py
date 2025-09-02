nums = [3,2,2,3]
val =3

def removeElement(nums: list[int], val: int) -> int:
    start = 0
    end = len(nums) - 1
    count = 0
    while start<end:
        if nums[start]==val:
            if nums[end]!=val:
                nums[start],nums[end]=nums[end],nums[start]
            end-=1
        else:
            start+=1
            count+=1
    return len(nums[:end+1])

print(removeElement(nums=nums,val=val))