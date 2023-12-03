from typing import List

class Solution:
    """
    For any bar i the maximum rectangle is of width r - l - 1 where r - is the last coordinate of the bar to the right with height h[r] >= h[i] and l - is the last coordinate of the bar to the left which height h[l] >= h[i]
    So if for any i coordinate we know his utmost higher (or of the same height) neighbors to the right and to the left, we can easily find the largest rectangle:
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        # store heights in ascending order
        stack = []
        i = 0
        max_area = 0

        while i < len(heights):
            # if current height >= top of stack, keeps append the index to the stack
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            # If this bar is lower than top of stack, 
            # then calculate area of rectangle with stack top as the smallest (or minimum height) bar.
            # 'i' is 'right index' for the top and 
            # element before top in stack is 'left index' 
            else:
                stack_top_idx = stack.pop()
                if stack:
                    area = heights[stack_top_idx] * (i - stack[-1] - 1)
                else:
                    area = heights[stack_top_idx] * (i)
                
                max_area = max(max_area, area)
        
        # Now pop the remaining bars from stack and 
        # calculate area with every popped bar as the smallest bar         
        while stack:
            stack_top_idx = stack.pop()

            # Calculate the area with  histogram[top_of_stack] stack as smallest bar 
            if stack:
                area = heights[stack_top_idx] * (i - stack[-1] - 1)
            else:
                area = heights[stack_top_idx] * (i)
            
            max_area = max(max_area, area)
        
        return max_area

mySol = Solution()
heights = [2,1,5,6,2,3]
max_area = mySol.largestRectangleArea(heights)
print(max_area)

heights = [2,4]
max_area = mySol.largestRectangleArea(heights)
print(max_area)

