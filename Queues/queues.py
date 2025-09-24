
"""
Queue is a linear data structure that follows the FIFO (First In First Out) principle. This means that the first element added to the queue will be the first one to be removed.
Queues are commonly used in scenarios such as task scheduling, resource management, and breadth-first search algorithms.

Queue supports the following operations:
- Enqueue: Add an element to the end of the queue.
- Dequeue: Remove and return the element at the front of the queue.
- Peek/Front: Return the element at the front of the queue without removing it.
- IsEmpty: Check if the queue is empty.
- Size: Return the number of elements in the queue.

from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
        
# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.size())     # Output: 2
q.empty()    # Output: False

Queues can be implemented using arrays or linked lists. The choice of implementation can affect the performance of the queue operations.

For thread safety we can use queue module in python
import queue
q = queue.Queue()
q.put(1)
q.put(2)
print(q.get())  # Output: 1
print(q.qsize())  # Output: 1
print(q.empty())  # Output: False
print(q.full())  # Output: False

The full method checks if the queue has reached its maximum size, which can be set when creating the queue (default is infinite size).
Example for setting max size:
q = queue.Queue(maxsize=3)

"""