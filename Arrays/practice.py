nums = [3,2,2,3]
val =3

def removeElement(nums: list[int], val: int) -> int:
    start = 0
    end = len(nums)-1
    while start <=end:
        if nums[start]!=val:
            start+=1
        else:
            if nums[end]==val:
                end-=1
            else:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
    return start
            

# print(removeElement(nums=nums,val=val))


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    from collections import Counter
    anagram_set=set()
    for string in strs:
        if Counter(string) not in anagram_set:
            anagram_set.add(Counter(string))
    return anagram_set
strs=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))