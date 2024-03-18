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

        for i in range(1, N):
            if max_left[i - 1] <= min_right[i]:
                return i

mySol = Solution()
nums = [5,0,3,8,6]
print(mySol.partitionDisjoint(nums))

# nums = [1,1,1,0,6,12]
# print(mySol.partitionDisjoint(nums))