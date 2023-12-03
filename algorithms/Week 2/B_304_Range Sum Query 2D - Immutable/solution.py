from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        while j < len(nums):
            nums[j] = 0
            j += 1
    
    def moveZeroes2(self, nums):
        # move non zero element to the left and zero to the right 
        temp = -1
        i = 0

        while i < len(nums):
            if temp == -1 and nums[i] == 0:
                temp = i
            elif temp != -1 and nums[i] != 0:
                nums[temp], nums[i] = nums[i], 0
                i = temp
                temp = -1
            i += 1


mySol = Solution()
# arr = [0,1,0,3,3,12]
# mySol.moveZeroes(arr)
# print(arr)

arr2 = [0,1,0,3,3,12]
mySol.moveZeroes2(arr2)
print(arr2)

