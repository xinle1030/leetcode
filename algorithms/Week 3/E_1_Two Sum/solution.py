from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in map:
                map[num] = i
            else:
                return [map[complement], i]
            

mySol = Solution()

nums = [2,7,11,15]
target = 9
print(mySol.twoSum(nums, target))

nums = [3,2,4]
target = 6
print(mySol.twoSum(nums, target))

nums = [3,3]
target = 6
print(mySol.twoSum(nums, target))