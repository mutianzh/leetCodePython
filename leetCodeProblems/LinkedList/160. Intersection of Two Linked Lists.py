"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # approach 1: calculate the length of two lists and two pointers
        node_a = headA
        len_a = 0
        while node_a:
            len_a += 1
            node_a = node_a.next

        node_b = headB
        len_b = 0
        while node_b:
            len_b += 1
            node_b = node_b.next

        diff = abs(len_a - len_b)
        long_list_node = headA if len_a > len_b else headB
        short_list_node = headB if len_a > len_b else headA
        while diff > 0:
            diff -= 1
            long_list_node = long_list_node.next

        while long_list_node and short_list_node:
            if long_list_node == short_list_node:
                return long_list_node

            long_list_node = long_list_node.next
            short_list_node = short_list_node.next

        return None