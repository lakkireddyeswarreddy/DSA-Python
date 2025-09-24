

def firstUniqChar(s: str) -> int:
    char_index_dict = {}
    for index,char in enumerate(s):
        if char in char_index_dict:
            char_index_dict[char]=-1
        else:
            char_index_dict[char]=index
        
    print(char_index_dict)
    for key in char_index_dict:
        if char_index_dict[key]!=-1:
            return char_index_dict[key]
    return -1

s="loveleetcode"
# print(firstUniqChar(s))

s="cbbd"

print(s[0:0])

def longestPalindrome(s: str) -> str:
    longest_palindronic_substring=""
    
    def expand_around_center(left,right):
        left=i
        right=i
        #odd length palindromic substring
        while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
        return s[left+1:right]
        
    for i in range(len(s)):
        palindrome = expand_around_center(left=i,right=i)
        if len(palindrome)>len(longest_palindronic_substring):
            longest_palindronic_substring=palindrome
            
        palindrome = expand_around_center(left=i,right=i+1)
        if len(palindrome)>len(longest_palindronic_substring):
            longest_palindronic_substring=palindrome
            
    return longest_palindronic_substring
                
# print(longestPalindrome(s))

def countSubstrings(s: str) -> int:
    palindromic_substrings=[]
    def expand_around_center(left,right,palindromic_substrings):
        while left>=0 and right<len(s) and s[left]==s[right]:
            palindromic_substrings.append(s[left:right+1])
            left-=1
            right+=1

    for i in range(len(s)):
        expand_around_center(i,i,palindromic_substrings)
        expand_around_center(i,i+1,palindromic_substrings)
    return palindromic_substrings

s="aaa"
print(countSubstrings(s))
            
            
def validPalindrome(s: str) -> bool:
    def is_palindrome(left,right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return is_palindrome(left+1,right) or is_palindrome(left,right-1)
        left+=1
        right-=1
    return True
        
            


        