from typing import List

"""
Two Pointer Solution

- A ith bar can trap the water if and only if there exists a higher bar to the left and a higher bar to the right of ith bar.
- To calculate how much amount of water the ith bar can trap, we need to look at the maximum height of the left bar and the maximum height of the right bar, then
- The water level can be formed at ith bar is: waterLevel = min(maxLeft[i], maxRight[i])
- If waterLevel >= height[i] then ith bar can trap waterLevel - height[i] amount of water.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # exclude the leftmost and rightmost from calculation as leftmost and rightmost cannot trap water
        left = 1
        right = n - 2
        maxLeft = height[0]
        maxRight = height[n - 1]

        water = 0

        while left <= right:
            # trapped water determined by smaller one
            if maxLeft < maxRight:
                water += max(0, maxLeft - height[left])

                maxLeft = max(maxLeft, height[left])

                left += 1
            else:
                water += max(0, maxRight - height[right])

                maxRight = max(maxRight, height[right])

                right -= 1
        
        return water

                
mySol = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
water = mySol.trap(height)
print(water)

height = [4,2,0,3,2,5]
water = mySol.trap(height)
print(water)