# temperatures = [73,74,75,71,69,72,76,73]

# def dailyTemperatures(temperatures: list[int]) -> list[int]:
#     temp_stack=[]
#     answer = [0] * len(temperatures)
#     for temp in temperatures:
#         if temp_stack is None:
#             temp_stack.append(temp)



def decodeString(s: str) -> str:
    temp_stack=[]
    output_str=""
    for char in s:
        temp_str=""
        if char!="]":
            temp_stack.append(char)
        else:
            while temp_stack:
                if temp_stack[-1]!="[":
                    temp_str=temp_stack.pop()+temp_str
                else:
                    temp_stack.pop()
                    repeat_number=""
                    while temp_stack[-1].isdigit():
                        repeat_number=temp_stack.pop()+repeat_number
                    temp_str=temp_str*int(repeat_number)
                    if not temp_stack:
                        output_str+=temp_str
                    else:
                        temp_stack.append(output_str)
                    break
    return output_str


print(decodeString("3[a]2[bc]")) # Output: "aaabcbc"

