
"""
Strings are immutable in python, this isn't a flaw, this offers a performance benefit. Since strings are immutable they can be used as keys as the hash() method returns the same value.
As strings are immutable they can be shared across the threads.
It even makes optimizations like using the same memory for identitical strings as they cannot be changed.

"""

"""Reversing a list inplace using two pointers"""

# def reverse_list(string_list =list[str]) -> list[str]:  # time complexity O(n), space complexity O(1) as we didn't use any extra space.
#     print(f"before reversing = {id(string_list)}")
#     start = 0
#     end = len(string_list)-1
    
#     while start < end:
#         string_list[start], string_list[end]=string_list[end],string_list[start]
#         start+=1
#         end-=1
#     print(f"after reversing = {id(string_list)}")
#     return string_list

string_list = ["e", "s", "w", "a", "r"]


"""Reversing a list in place using recursion"""

def reverse_list(string_list): # time complexity is O(n), space complexity is O(n) as it needs to keep track of the function calls in the call stack, so two pointer method is more efficient.
    
    def reverse(start, end):
        if start>=end:
            return
        string_list[start],string_list[end]=string_list[end],string_list[start]
        reverse(start+1,end-1)
    reverse(start=0,end=len(string_list)-1)
    return string_list

# print(reverse_list(string_list))

moves=0

def hanoi(n, src, dest, aux):
    global moves
    if n==1:
        moves+=1
        return
    hanoi(n-1,src,aux, dest)
    moves+=1
    hanoi(n-1,aux,dest,src)
    return moves

print(hanoi(2,"a","b","c"))


def reverse_string(s:list[str]):
    pass
    
