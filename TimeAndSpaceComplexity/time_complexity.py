"""
Time complexity is a way to analyze the efficiency of an algorithm, generally time complexity is expressed in terms of Big-O Notation, which is the worst case or the upper bound.

Time complexity is expressed mainly in three notations : 

1.Big-O : it describes the worst case, this means algorithms execution time can grow maximum upto the specified time.
2.Omega : it describes the best case, this means algorithms execution time can grow minimum upto the specified time.
3.Theta : it describes the average case or the tight bound, if the omega and the Big-O are same then Theta = Big-O = omega. If they are different you need to analyze the algorithm
for calculating the theta notation.

"""

nums = [1, 2, 3, 4]

def print_nums(nums):
    for num in nums: pass
        # print(num) # n operations in all cases
        
"""
time complxeity for printing all the numbers is same in both the worst, average and best case. So in all notations the time complexity is same O(n)=omega(n)=theta(n)
"""
print_nums(nums)

def find_element_in_array(nums, element):
    for num in nums: # constant time in best case if the element find at the first index linear time in worst case if the element at the last index or if the element doesn't find.
        if num == element: # n operations in worst case , 1 operation in best case.
            print("found element")
            break
        
"""
For an average case, if element is present in the array then it may be at any position from 1 to n, so the probabilty is 1/n for any position.
If the element is present in the kth position then we need to make the k comparisons which means k operations so T(n) = (1+2+..k+..n)/n === (n+1)/2 operations on an average
If the elemtnt is not present then we need to perform n operation so n

If the probablity of an element to exist in the array is p then not extists is 1-p so p(n+1)/2 + (1-p)n == n

"""


"""
Fibonacci seqeunce is an ordered list of numners, where each fibonnaci number is the sum of its two preceeding numbers, with base case starting from 0,1.
And each fibonnaci number is any number in the sequence where sum equals to the sum of two preceeding numbers.
"""

def fibonnaci(num):
    # fibonnaci_sequence = [0,1]
    # for i in range(2,num+1):
    #     fibonnaci_sequence.append(fibonnaci_sequence[i-1]+fibonnaci_sequence[i-2])
    # return fibonnaci_sequence[-1]
    
    a=0
    b=1
    for i in range(2,num+1):
        c = a+b
        a=b
        b=c
    return b
    
    if num <=1:
        return num
    return fibonnaci(num-1) + fibonnaci(num-2) # recursive fibonnaci has O(2*n) time complexity without memoization, as there are two recursive calls for each number, and it has O(height of the recursion tree) space complexity for the call stack.

print(fibonnaci(10))

 