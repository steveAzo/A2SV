# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        curr = head
        while curr:
            if curr in node_set:
                return True
            node_set.add(curr)
            curr = curr.next
        
        return False
        