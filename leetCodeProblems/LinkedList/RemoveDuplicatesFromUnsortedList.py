"""
1836. Remove Duplicates From an Unsorted Linked List
Given the head of a linked list, find all the values that appear more than once in the list and delete the nodes that have any of those values.

Return the linked list after the deletions.
Example 1:
Input: head = [1,2,3,2]
Output: [1,3]
Explanation: 2 appears twice in the linked list, so all 2's should be deleted. After deleting all 2's, we are left with [1,3].
Example 2:
Input: head = [2,1,1,2]
Output: []
Explanation: 2 and 1 both appear twice. All the elements should be deleted.
Example 3:
Input: head = [3,2,2,1,3,2,4]
Output: [1,4]
Explanation: 3 appears twice and 2 appears three times. After deleting all 3's and 2's, we are left with [1,4].
Constraints:
The number of nodes in the list is in the range [1, 105]
1 <= Node.val <= 105

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = dict()
        dup = dict()

        current = head

        # Find all duplicated values
        while current:
            if current.val in seen:
                # This is a duplicated value
                dup[current.val] = True
            else:
                seen[current.val] = True

            current = current.next

        # Remove all duplicated values
        current = head
        dummy_head = ListNode(0, head)
        dummy_end = dummy_head
        while current:
            if current.val in dup:
                dummy_end.next = current.next
            else:
                dummy_end = dummy_end.next

            current = current.next

        return dummy_head.next




