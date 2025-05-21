# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        running_list = dummy

        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                running_list.next = curr1
                running_list = running_list.next
                curr1 = curr1.next
            else:
                running_list.next = curr2
                running_list = running_list.next
                curr2 = curr2.next
        
        while curr1:
            running_list.next = curr1
            running_list = running_list.next
            curr1 = curr1.next
        while curr2:
            running_list.next = curr2
            running_list = running_list.next
            curr2 = curr2.next
        
        return dummy.next