"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        prev = None
        thir = curr.next

        cnt = 1
        while cnt < left:
            prev = curr
            curr = curr.next
            cnt += 1

        # Now the cnt is equal to left, and curr is the left-th node
        cons = prev
        tail = curr

        while cnt <= right:
            thir = curr.next
            curr.next = prev
            prev = curr
            curr = thir
            cnt += 1

        if cons:
            cons.next = prev
        else:
            head = prev

        tail.next = curr
        return head