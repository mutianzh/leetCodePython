"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from collections import Counter
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #         # bucket sort
        #         buckets = [[] for _ in range(len(nums))]
        #         counter = Counter(nums).items()
        #         for item, freq in counter:
        #             buckets[freq - 1].append(item)

        #         res = []
        #         for bucket in buckets:
        #             res += bucket

        #         return res[-k:]

        # quick select
        count = Counter(nums)
        unique_list = list(set(nums))

        def patition(left, right, pivot):
            if left == right:
                return left

            # swap pivot and right most element
            unique_list[pivot], unique_list[right] = unique_list[right], unique_list[pivot]

            # patition the list
            store_index = left
            for i in range(left, right + 1, 1):
                if count[unique_list[i]] < count[unique_list[right]]:
                    unique_list[store_index], unique_list[i] = unique_list[i], unique_list[store_index]
                    store_index += 1

            # swap pivot with store_index
            unique_list[store_index], unique_list[right] = unique_list[right], unique_list[store_index]

            return store_index

        def quick_find(left, right, good_location):
            # randomly select a pivot
            pivot = random.randint(left, right)

            pivot = patition(left, right, pivot)

            if pivot == good_location:
                return
            elif pivot < good_location:
                quick_find(pivot + 1, right, good_location)
            else:
                quick_find(left, pivot - 1, good_location)

        length = len(unique_list)
        quick_find(0, length - 1, length - k)
        return unique_list[-k:]