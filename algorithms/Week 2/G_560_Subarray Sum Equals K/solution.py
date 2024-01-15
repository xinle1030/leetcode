from typing import List
from collections import defaultdict

"""
Concept use prefix sum (cumulative sum)
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currentSum = 0

        prevSum = defaultdict(int)

        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum == k:
                count += 1
            
            # currsum exceeds given sum by currsum  - sum.
            # Find number of subarrays having  
            # this sum and exclude those subarrays 
            # from currsum by increasing count by  
            # same amount. 
            if (currentSum - k) in prevSum:
                count += prevSum[currentSum - k]
            
            # Add currsum value to count of  
            # different values of sum. 
            prevSum[currentSum] += 1

        return count

mySol = Solution()

nums = [1,1,1]
k = 2
print(mySol.subarraySum(nums, k))

nums = [1,2,3]
k = 3
print(mySol.subarraySum(nums, k))

