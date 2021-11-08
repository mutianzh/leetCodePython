"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: The given linked list is empty (null pointer), so return null.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        # step 1: insert copied nodes with copied values
        curr_node = head
        while curr_node:
            new_node = Node(curr_node.val, curr_node.next, None)
            curr_node.next = new_node
            curr_node = new_node.next

        # step 2: copy random pointers
        curr_node = head
        while curr_node:
            new_curr = curr_node.next
            if curr_node.random:
                new_curr.random = curr_node.random.next
            curr_node = curr_node.next.next

        # step 3: seperate copied nodes
        new_head = head.next
        curr_node = head
        while curr_node:
            new_curr = curr_node.next
            curr_node.next = curr_node.next.next
            if curr_node.next:
                new_next = curr_node.next.next
            else:
                new_next = None
            new_curr.next = new_next

            curr_node = curr_node.next

        return new_head