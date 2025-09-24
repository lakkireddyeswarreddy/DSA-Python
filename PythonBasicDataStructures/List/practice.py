 
nested_list = [1, 2, [3, 4], [5, [6, 7], 8]]


def flatten_nested_list(nested_list):
    output_list=list()
    
    #Recursive approach
    #Recursion depth is equal to the depth of the nested list.
    #Has O(depth) space complexity excluding the output_list
    # for element in nested_list:
    #     if isinstance(element,list):
    #         output_list.extend(flatten_nested_list(element))
    #     else:
    #         output_list.append(element)
            
    stack=[nested_list]
    
    while stack:
        stack_element= stack.pop()
        for element in stack_element:
            if isinstance(element,list):
                stack.append(element)
            else:
                output_list.append(element)
    
    return output_list

print(flatten_nested_list(nested_list))