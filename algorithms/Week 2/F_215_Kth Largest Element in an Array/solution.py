from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums)

        while True:
            p = random.randint(low, high - 1)
            m, pi = self.partition(nums, low, high, p)
            if m < k <= pi:    # from m th largest to i th largest they are the same, and k is among them
                return nums[m]
            elif k <= m:
                high = m
            elif k > pi:
                low = pi
    
    def partition(self, arr, low, high, p):
        pivot = arr[p]

        # pointer for greater element
        i = low + 1

        arr[p], arr[low] = arr[low], arr[p]

        # traverse through all elements
        # compare each element with pivot
        while i < high:
            if arr[i] > pivot:
                arr[i], arr[low] = arr[low], arr[i]
                i += 1
                low += 1
            elif arr[i] == pivot:
                i += 1
            else:
                high -= 1
                arr[i], arr[high] = arr[high], arr[i]
        
        # low, ..., i
        return low, i
            
mySol = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(mySol.findKthLargest(nums, k))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(mySol.findKthLargest(nums, k))

nums = [1]
k = 1
print(mySol.findKthLargest(nums, k))