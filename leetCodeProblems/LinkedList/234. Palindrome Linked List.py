"""
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        #         # sol 1: store val in a list, O(n) and O(n)
        #         val = []
        #         cur_node = head
        #         while cur_node:
        #             val.append(cur_node.val)
        #             cur_node = cur_node.next

        #         return val == val[::-1]

        # sol 2: reverse half of the list
        # Find the middle of linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If even number, now slow points at the first node of second half
        # If odd number, new slow pints at the middle
        # Reverse the remaining list
        node = None  # node is the current head of reversed list
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        # Compare
        while node:
            if node.val != head.val:
                return False

            node = node.next
            head = head.next

        return True