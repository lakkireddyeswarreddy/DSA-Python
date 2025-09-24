
"""
Two pointers is a programming paradigm that uses two pointers to iterate through the data structure.
It is used to reduce the time complexity of the algorithm.
It is mainly used in arrays and linked lists.

There are two types of two pointers:
1. Opposite direction two pointers: In this we use two pointers, one pointer starts from the beginning of the array and the other pointer starts from the end of the array, and they move towards each other until they meet.
2. Same direction two pointers: In this we use two pointers, both pointers start from the beginning of the array, and one pointer moves faster than the other pointer.

Sliding window is a special case of same direction two pointers, in this we use two pointers to create a window of fixed size, and we move the window by moving both pointers at the same time.
window can be of fixed size or variable size.
It is mainly used to find the subarray or substring that satisfies a particular condition.

fixed size window example: find the maximum sum of k consecutive elements in an array.
variable size window example: find the smallest subarray with a sum greater than or equal to a given value.

"""



def is_palindromw(s:str) -> bool:
    left = 0
    right = len(s) -1
    
    while left < right:
        while left < right and not s[right].isalnum():
            right -=1
        while left < right and not s[left].isalnum():
            left+=1
        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True

nums1=[4,5,6,0,0,0]
nums2=[1,2,3]
m=3
n=3
# [1,2,3,0,0,0]
# [2,5,6]
# nums1=[1]
# nums2=[]
# m=1
# n=0

# nums1=[0]
# nums2=[1]
# m=0
# n=1
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m-1
    j= n-1
    k=m+n-1
    while i>=0 and j>=0:
        if nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i-=1
        else:
            nums1[k]=nums2[j]
            j-=1
        k-=1
    while j>=0:
        nums1[k]=nums2[j]
        j-=1
        k-=1
        
    return nums1
# print(merge(nums1,m,nums2,n))

nums = [-1,0,1,2,-1,-4]

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort() # [-4,-1,-1,0,1,2]
    output_list = []
    i=0
    while i<len(nums)-2:
        if i>0 and nums[i]==nums[i-1]:
            continue
        start = i+1
        end = len(nums)-1
        while start<end:
            if nums[i] + (nums[start]+nums[end])==0:
                output_list.append([nums[i],nums[start],nums[end]])
                while start<end and nums[start]==nums[start+1]:
                    start+=1
                while start<end and nums[end]==nums[end-1]:
                    end-=1
                start+=1
                end-=1
            elif nums[i]+ (nums[start]+nums[end])>0:
                end-=1
            else:
                start+=1
        i+=1
    return output_list
        
            
# print(threeSum(nums))
    
s="abcabcbb"

def lengthOfLongestSubstring(s: str) -> int:
    
    left=0
    right=0
    max_length=0
    # char_set=set()
    # for right, element in enumerate(s):
    #     if element in char_set:
    #         while element in char_set:
    #             char_set.remove(s[left])
    #             left+=1
    #     char_set.add(element)
    #     max_length=max(max_length,right-left+1)
    
    char_index_set= dict()
    for right, element in enumerate(s):
        if element in char_index_set and char_index_set[element]>=left:
            left = char_index_set[element]
        char_index_set[element]=right
        max_length=max(max_length,right-left+1)
    
    return max_length

# print(lengthOfLongestSubstring(s))

def maxArea(self, height: list[int]) -> int:
    pass

s = "a"
t = "aa"
def minWindow(s: str, t: str) -> str:
    sub_string_dict={}
    for char in t:
        sub_string_dict[char]=""
    for i,char in enumerate(s):
        if char in sub_string_dict:
            sub_string_dict[char]=i
    if "" in sub_string_dict.values():
        return ""
    max_index=max(sub_string_dict.values())
    min_index=min(sub_string_dict.values())
    return s[min_index:max_index+1]

print(minWindow(s,t))
    