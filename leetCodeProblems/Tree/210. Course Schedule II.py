"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""

import collections
class Solution(object):

    # # Solution 1: DFS
    # def __init__(self):
    #     self.white = 1
    #     self.grey = 2
    #     self.black = 3
    #     self.is_possible = True  # No cycle exits.
    #
    # def findOrder(self, numCourses, prerequisites):
    #
    #     ans = []
    #     # Construct the graph use dictionary
    #     graph = collections.defaultdict(list)
    #     for des, src in prerequisites:
    #         graph[src].append(des)
    #
    #     # Initialize the color of each node
    #     # Black: The node has already been added in to the stack
    #     # Grey: The node we are currently exploring
    #     # White: The node is not explored
    #     colors = {i: self.white for i in range(numCourses)}
    #
    #     # Define the DFS function to explore each node
    #     def dfs(node):
    #
    #         if colors[node] == self.grey:
    #             self.is_possible = False
    #             return
    #
    #         elif colors[node] == self.black:
    #             pass
    #             # Do nothing
    #         elif colors[node] == self.white:
    #             if node in graph:
    #                 colors[node] = self.grey
    #                 for child in graph[node]:
    #                     dfs(child)
    #             ans.append(node)
    #             colors[node] = self.black
    #
    #     # For each node that is not explored yet, run dfs
    #     for i in range(numCourses):
    #         if colors[i] == self.white:
    #             dfs(i)
    #
    #     return ans[::-1] if self.is_possible else []

    # Solution 2: Kahn's algorithm
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Store graph into a dict
        # Initialize the in-degrees for each node
        # in_degree is the number of prerequisites for each course
        graph = collections.defaultdict(list)
        in_degrees = collections.defaultdict(int)
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degrees[dest] += 1

        ans = []
        queue = collections.deque()
        # Add nodes with zero in_degrees into the queue
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            ans.append(node)
            for child in graph[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    queue.append(child)

        return ans if len(ans) == numCourses else []


num = 4
order = [[1,0],[2,0],[3,1],[3,2]]

# num = 2
# order = [[1,0]]

# num = 2
# order = [[1,0], [0,1]]

# num = 3
# order = []

num = 3
order = [[0,1],[0,2],[1,2]]

solution = Solution()
print(solution.findOrder(num, order))