from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return f"Node with value {self.val}"
        
node1=ListNode(1)
node2=ListNode(4)
node3=ListNode(7)
node4=ListNode(9)
# node5=ListNode(3)
# node6=ListNode(4)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1
# node5.next = node6


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return 



# print(reverseList(node1))


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    first = head
    second = head.next
    while first and second:
        if first.val==second.val:
            first.next=None
            second=second.next
        else:
            first.next=second
            first=first.next
            second=second.next
    return head

# print(deleteDuplicates(node1))

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head_combined=None
    temp=None
    while list1 and list2:
        if list1.val<list2.val:
            if temp is None:
                temp=list1
            else:
                temp.next=list1
                temp=temp.next
            list1=list1.next
        else:
            if temp is None:
                temp=list2
            else:
                temp.next=list2
                temp=temp.next
            list2=list2.next
        if head_combined is None:
            head_combined=temp
    if list1:
        if temp is None:
            temp=list1
            head_combined=temp
        else:
            temp.next=list1 
    if list2:
        if temp is None:
            temp=list2
            head_combined=temp
        else:
            temp.next=list2 
    return head_combined
    
# list1=node1
# list2=node4

# print(mergeTwoLists(list1,list2))

def sortedInsert(head, data):
    current=head
    previous=current
    current=current.next
    new_node=ListNode(data)
    while current:
        print(current.val)
        if previous.val<=new_node.val and new_node.val<=current.val:
            new_node.next=current
            previous.next=new_node
            break
        current=current.next
        if current.next == head:
            new_node.next=head
            current.next=new_node
            break
    return head

print(sortedInsert(node1,5))


            