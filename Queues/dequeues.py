"""
Dequeues (Double-Ended Queues):
Dequeues support the following operations:
- Add to Front: Add an element to the front of the deque.
- Add to Rear: Add an element to the rear of the deque.
- Remove from Front: Remove and return the element at the front of the deque.
- Remove from Rear: Remove and return the element at the rear of the deque.
- Peek Front: Return the element at the front of the deque without removing it.
- Peek Rear: Return the element at the rear of the deque without removing it.
- IsEmpty: Check if the deque is empty.
- Size: Return the number of elements in the deque.
from collections import deque

example usage:
dq = deque()    # Create an empty deque
dq.append(1)    # Add 1 to the rear of the deque
dq.appendleft(2) # Add 2 to the front of the deque      
dq.pop()        # Remove and return the rear element (1)
dq.popleft()    # Remove and return the front element (2)
dq.append(3)
dq.append(4)
print(dq)       # Output: deque([3, 4])
dq.extend([5, 6]) # Add multiple elements to the rear
print(dq)       # Output: deque([3, 4, 5, 6])
dq.extendleft([1, 2]) # Add multiple elements to the front (note the order is reversed)
print(dq)       # Output: deque([2, 1, 3, 4, 5, 6])
print(dq[0])    # Peek front element (2)
print(dq[-1])   # Peek rear element (6)
print(dq.is_empty()) # Output: False
print(dq.size()) # Output: 6
len(dq)        # Output: 6

Length of deque can be found using len() function and is_empty can be checked using len(dq) == 0
size() can be implemented as a method if needed. 
Implementation of size() and is_empty() methods:
class Deque:
    def __init__(self):
        self.deque = deque()
    
    def is_empty(self):
        return len(self.deque) == 0
    
    def size(self):
        return len(self.deque)
        
# Example usage:
dq = Deque()
print(dq.is_empty()) # Output: True
print(dq.size())     # Output: 0


Double-ended queues (deques) can be implemented using arrays or linked lists. In Python, we can use the collections.deque class which is optimized for fast fixed-time appends and pops from both ends.
By default, deque has no maximum size. However, we can set a maximum size when creating the deque. If the deque is full, adding a new element will automatically remove an element from the opposite end.
dq = deque(maxlen=3)
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)       # Output: deque([1, 2, 3], maxlen=3)
dq.append(4)
print(dq)       # Output: deque([2, 3, 4], maxlen=3)
If we try to append to a full deque, the oldest element (from the opposite end) is removed to make space for the new element.
Applications of Deque:
- Palindrome Checker: Deques can be used to check if a string is a palindrome by comparing characters from both ends.
- Sliding Window Problems: Deques are useful for maintaining a list of elements in a sliding window fashion.- Task Scheduling: Deques can be used to manage tasks that need to be processed in both FIFO and LIFO order.
- Undo/Redo Functionality: Deques can be used to implement undo and redo functionality in applications by maintaining a history of actions.

"""