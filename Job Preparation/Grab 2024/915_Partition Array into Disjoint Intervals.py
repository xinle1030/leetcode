from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        max_left = [None] * N
        min_right = [None] * N
        
        max_left[0] = nums[0]
        min_right[-1] = nums[-1]

        for i in range(1, N):
            max_left[i] = max(max_left[i - 1], nums[i])

        for i in range(N - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])

        print(max_left)
        print(min_right)
        print()

        """
        Check for each index i if the maximum value from the left (max_left[i - 1]) is <= the minimum value from the right (min_right[i]). 
        The first index i where this condition is met indicates the partition point.

        The condition "max_left[i - 1] <= min_right[i]" ensures that the left subarray can be extended up to index i without violating the condition that every element in the left subarray is less than or equal to every element in the right subarray.
        """
        for i in range(1, N):
            if max_left[i - 1] <= min_right[i]:
                return i

mySol = Solution()
nums = [5,0,3,8,6]
print(mySol.partitionDisjoint(nums))

# nums = [1,1,1,0,6,12]
# print(mySol.partitionDisjoint(nums))