test_dict = {
    "Key1" : "1",
    "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                        "d" : {"x":{"y": "10"}},
                        "e" : "1"
                        }
                }
            }




def flatten_dictionary(test_dict) ->dict:
    output_dict={}
    
    stack=[("",test_dict)]
    
    while stack:
        prefix,stack_element = stack.pop()
        for element in stack_element:
            if isinstance(stack_element[element],dict):
                stack.append((f"{prefix}.{element}", stack_element[element]) if prefix  else (f"{element}", stack_element[element]))
            else:
                output_dict[f"{prefix}.{element}" if prefix else f"{element}"]=stack_element[element]
                
    return output_dict
                
    
    # def flatten_inner_dict(outer_key,d):
    #     for key in d:
    #         if isinstance(d.get(key), dict):
    #             flatten_inner_dict(f"{outer_key}.{key}",d.get(key))
    #         else:
    #             output_dict[f"{outer_key}.{key}"]=d.get(key)
    
    # for key in test_dict:
    #     if isinstance(test_dict.get(key), dict):
    #         flatten_inner_dict(key,test_dict.get(key))
    #     else:
    #         output_dict[f"{key}"]=test_dict.get(key)
            
        
    # return output_dict

print(flatten_dictionary(test_dict))
            