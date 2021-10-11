"""
1213. Intersection of Three Sorted Arrays
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
Example 2:

Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []


Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""


class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        if arr1 and arr2 and arr3:
            len_1 = len(arr1)
            len_2 = len(arr2)
            len_3 = len(arr3)

            if min([len_1, len_2, len_3]) == 0:
                return []
            else:
                results = []
                p1 = 0
                p2 = 0
                p3 = 0
                while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
                    if arr1[p1] == arr2[p2] == arr3[p3]:
                        results.append(arr1[p1])
                        p1 += 1
                        p2 += 1
                        p3 += 1
                    elif arr1[p1] < arr2[p2]:
                        p1 += 1
                    elif arr2[p2] < arr3[p3]:
                        p2 += 1
                    else:
                        p3 += 1

                return results



        else:
            return []