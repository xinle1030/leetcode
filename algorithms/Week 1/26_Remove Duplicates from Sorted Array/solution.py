from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                # shift unique item to left 
                j += 1  
                nums[j] = nums[i]
        return j + 1
    
mySol = Solution()
arr = [1, 2, 2, 2, 3, 4, 4, 5, 5, 6]
print(mySol.removeDuplicates(arr))