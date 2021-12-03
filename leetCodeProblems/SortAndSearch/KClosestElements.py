"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

"""

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        target = x
        mid = 0
        
        if len(arr) <= k:
            return arr
        
        low = 0
        high = len(arr) - 1
        
        while low + 1 < high:
            mid = int(low + (high - low)/2)
            
            if arr[mid] == target:
                break
            elif arr[mid] > target:
                high = mid
            else:
                low = mid
                
        result = []
        if arr[mid] == target:
            result.append(arr[mid])
            
            left = mid - 1
            right = mid + 1
            
            while len(result) < k:
                if left < 0:
                    if right <= len(arr) - 1:
                        result.append(arr[right])
                        right += 1
                    else:
                        return result
                
                elif right > len(arr) - 1:
                    if left >= 0:
                        result.insert(0, arr[left])
                        left -= 1
                    else:
                        return result
                    
                else:
                    if abs(arr[right] - target) < abs(arr[left] - target):
                        result.append(arr[right])
                        right += 1
                    else:
                        result.insert(0,arr[left])
                        left -= 1
            
        else:
            left = low
            right = high
        
            while len(result) < k:
                if left < 0:
                    if right <= len(arr) - 1:
                        result.append(arr[right])
                        right += 1
                    else:
                        return result
                
                elif right > len(arr) - 1:
                    if left >= 0:
                        result.insert(0, arr[left])
                        left -= 1
                    else:
                        return result
                    
                else:
                    if abs(arr[right] - target) < abs(arr[left] - target):
                        result.append(arr[right])
                        right += 1
                    else:
                        result.insert(0,arr[left])
                        left -= 1
        return result
