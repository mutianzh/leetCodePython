"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #         # method 1: hash table
        #         ans = []

        #         seen = collections.defaultdict(int)
        #         list1 = nums1 if len(nums1) < len(nums2) else nums2
        #         list2 = nums2 if len(nums1) < len(nums2) else nums1

        #         for num in list1:
        #             seen[num] += 1

        #         for num in list2:
        #             if seen[num] > 0:
        #                 ans.append(num)
        #                 seen[num] -= 1

        #         return ans

        # method 2: sort
        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()

        index1 = 0
        index2 = 0
        ans = []

        size1 = len(nums1)
        size2 = len(nums2)

        while index1 < size1 and index2 < size2:
            n1 = nums1[index1]
            n2 = nums2[index2]
            if n1 == n2:
                index1 += 1
                index2 += 1
                ans.append(n1)
            elif n1 < n2:
                index1 += 1
            else:
                index2 += 1

        return ans
