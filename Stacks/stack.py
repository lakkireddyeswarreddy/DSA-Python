"""
Stack is a linear data structure that follows the Last In First Out (LIFO) principle. This means that the last element added to the stack will be the first one to be removed.
It can be visualized as a collection of elements where you can only add or remove elements from the top of the stack.
It supports two primary operations:
1. Push: Adds an element to the top of the stack.
2. Pop: Removes and returns the top element from the stack.
Other common operations include:
- Peek/Top: Returns the top element without removing it.
- IsEmpty: Checks if the stack is empty.
Stack can be implemented using arrays or linked lists. In Python, we can use lists to implement stack functionality.
Here is a simple implementation of a stack in Python using a list:
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)
        
# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek()) # Output: 2
print(stack.size()) # Output: 2

# Flattening a nested list using stack
nested_list = [1, 2, [3, 4], [5, [6, 7], 8]]
def flatten_nested_list(nested_list):
    output_list = []
    stack = [nested_list]
    
    while stack:
        stack_element = stack.pop()
        for element in stack_element:
            if isinstance(element, list):
                stack.append(element)
            else:
                output_list.append(element)
    
    return output_list
print(flatten_nested_list(nested_list))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
The order of elements in the flattened list may vary based on the order of processing.

Applications of Stack:
1. Expression Evaluation: Stacks are used in evaluating expressions (infix, postfix, prefix).
2. Backtracking Algorithms: Stacks are used in algorithms like maze solving, puzzle solving, etc.
3. Function Call Management: The call stack in programming languages uses stacks to manage function calls and returns.

In multithreading we can use the Lifoqueue class from the queue module in python
import queue
stack = queue.LifoQueue()
stack.put(1)
stack.put(2)
print(stack.get())  # Output: 2
len(stack.queue)  # Output: 1
stack.size()  # Output: 1
stack.empty()  # Output: False
stack.full()  # Output: False

the full method checks if the stack has reached its maximum size, which can be set when creating the stack (default is infinite size).
Example for setting max size:
stack = queue.LifoQueue(maxsize=3)
"""