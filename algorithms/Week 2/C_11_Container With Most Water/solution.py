from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            min_height = min(height[left], height[right])
            area = min_height * (right - left)

            if area > max_area:
                max_area = area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

mySol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(mySol.maxArea(height))

height = [1,1]
print(mySol.maxArea(height))