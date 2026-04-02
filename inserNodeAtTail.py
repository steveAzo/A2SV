

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    
    if not head:
        head = new_node
        return head
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

