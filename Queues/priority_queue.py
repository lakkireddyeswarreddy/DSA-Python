"""
Priorrity queue is an special type of queue in which each element is associated with a priority.
Elements with higher priority are dequeued before elements with lower priority.
If two elements have the same priority, they are dequeued in the order they were added to the queue (FIFO order).

Priority queues can be implemented using arrays and heaps, but heaps are the most efficient way to implement them.
If we use arrays, the time complexity for insertion is O(1) but for deletion it is O(n) as we have to search for the highest priority element.
If we use heaps, both insertion and deletion can be done in O(log n) time.
Here is a simple implementation of a priority queue using the heapq module in Python:
import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
        
By default, heapq implements a min-heap, so the element with the lowest priority value is dequeued first.
# Example usage:
pq = PriorityQueue()
pq.put("task1", 2)
pq.put("task2", 1)
pq.put("task3", 3)
print(pq.get())  # Output: task2

To implement a max-heap, we can invert the priority values by multiplying them by -1 when adding to the heap and when retrieving from the heap.
pq.put("task1", -2) 
pq.put("task2", -1)
pq.put("task3", -3)
print(pq.get())  # Output: task3

For implementing thread safe priority queue we can use the queue module in python
import queue
pq = queue.PriorityQueue()
pq.put((2, "task1"))
pq.put((1, "task2"))
print(pq.get()[1])  # Output: task2


"""