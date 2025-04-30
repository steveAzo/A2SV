# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        frPointer = head
        bhPointer = head

        while frPointer and frPointer.next:
            frPointer = frPointer.next.next
            bhPointer = bhPointer.next
        
        return bhPointer
        