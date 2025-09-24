"""
Singly linked list is a linear data structure, where each element is stored in a separate object called a node. Each node contains two fields: data and a reference (or pointer) to the next node in the sequence.
The last node points to null, indicating the end of the list.
Unlike arrays, linked lists do not store elements in contiguous memory locations, allowing for efficient insertions and deletions.
So, you cannot access elements by index directly; instead, you must traverse the list from the head node to reach a specific element.
Insertion and deletion operations can be performed in constant time O(1) if the pointer to the node before the operation is known or if the operation is at the beginning.
Linked lists can be used to implement other data structures like stacks, queues.
Linked lists can be singly linked (each node points to the next node) or doubly linked (each node points to both the next and previous nodes).
Linked lists doesn't have the length property like arrays.

Node structure:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"Node with value {self.val}"
        
Linked list is represented by the head node.

Linked list structure:
class LinkedList:
    def __init__(self):
        self.head = None
        
This head node points to the first node in the list. If the list is empty, the head is None.


"""