
def shortestPalindrome(s: str) -> str:
    str_list=list(s)
    left=0
    right=len(str_list)-1
    while left<right:
        if str_list[left]!=str_list[right]:
            str_list.insert(left,str_list[right])
            right+=1
        else:
            left+=1
            right-=1
    return "".join(str_list)

s="abcd"
print(list(s))

# print(shortestPalindrome(s))

s="a good   example"
def reverseWords(s: str) -> str:
    str_list=[word.strip() for word in s.split(" ") if word!=""]
    left=0
    right=len(str_list)-1
    while left<right:
        str_list[left],str_list[right]=str_list[right],str_list[left]
        left+=1
        right-=1
    return str_list

print(reverseWords(s))