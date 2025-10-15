"""
Permutations is defined as number of unique ways you can arrange n numbers, order matters here.

Combinations is defined as number of ways you can select k numbers from n numbers, here the order doesn't matter.
"""
result=[]
def generate_permutations(nums, path, is_used ):
    if len(path)==len(nums):
        result.append(path.copy())
    for i in range(len(nums)):
        if not is_used[i]:
            is_used[i]=True
            path.append(nums[i])
            generate_permutations(nums, path, is_used)
            path.pop()
            is_used[i]=False

    return len(result)
nums=[1,2,3,4]
# print(generate_permutations(nums,[],[False] * len(nums)))

result=[]
def generate_combinations(nums,start, path, no_of_elements):
    if len(path)==no_of_elements:
        result.append(path.copy())

    for i in range(start, len(nums)):
        path.append(nums[i])
        generate_combinations(nums,i+1,path,no_of_elements)
        path.pop()

    return result

# print(generate_combinations(nums,0, [], 2))

result=[]
def generate_subsets(nums, start, path):
    result.append(path[:])
    for i in range(start, len(nums)):
        if i>start and nums[i]==nums[i-1]:
            continue
        path.append(nums[i])
        generate_subsets(nums,i+1,path)
        path.pop()

    return result

print(generate_subsets(nums, 0, []))