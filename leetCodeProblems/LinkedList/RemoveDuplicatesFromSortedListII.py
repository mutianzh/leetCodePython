"""
82. Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head
        first_good_node = None
        last_good_node = None  # last_good_node's next is the next node waiting to be checked

        while current_node:
            if current_node.next and current_node.next.val == current_node.val:
                while current_node.next and current_node.next.val == current_node.val:
                    current_node = current_node.next

                # when out of while, current_node is the last one in the sublist of repeated values
                # Skip the entire sublist and check the one next
                if last_good_node:
                    last_good_node.next = current_node.next


            else:
                # case 1: current_node has next not None and is a good node
                if first_good_node == None:
                    # current_node is the first good node
                    first_good_node = current_node
                    last_good_node = current_node
                else:
                    # current_node should be append to the last good node
                    last_good_node = last_good_node.next

                # case 2: current_node has next None, which is the last node
                # No more repeated will follow behind, so current_node should be a good node
                # Nothing needs to be done in this case

            current_node = current_node.next

        return first_good_node







