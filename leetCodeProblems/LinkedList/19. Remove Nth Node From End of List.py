"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(None)
        dummy_head.next = head

        slow = dummy_head
        fast = dummy_head
        count = n + 1
        while count > 0 and fast:
            fast = fast.next
            count -= 1

        # if n is larger than the length of the linked list
        if count > 0:
            return head

        while fast:
            slow = slow.next
            fast = fast.next

        to_be_delete = slow.next
        slow.next = slow.next.next
        del to_be_delete

        return dummy_head.next