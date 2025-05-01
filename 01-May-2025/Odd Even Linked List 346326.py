# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_nodes = ListNode(1)
        copy_odd = odd_nodes
        even_nodes = ListNode(0)
        copy_even = even_nodes
        
        i = 1
        curr = head
        while curr:
            if i % 2 == 1:
                odd_nodes.next = curr
                odd_nodes = odd_nodes.next
            else:
                even_nodes.next = curr
                even_nodes = even_nodes.next
            
            curr = curr.next
            i += 1
            
        if i % 2 == 0:
            even_nodes.next = None
        else:
            odd_nodes.next = None

        odd_nodes.next = copy_even.next
        return copy_odd.next
        