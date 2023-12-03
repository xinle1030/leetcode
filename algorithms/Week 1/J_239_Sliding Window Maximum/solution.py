from typing import List
from collections import deque

"""
Time Complexity: O(N). It seems more than O(N) at first look. It can be observed that every element of the array is added and removed at most once. So there are a total of 2n operations.
Auxiliary Space: O(K). Elements stored in the dequeue take O(K) space.

References: https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        # store index of the largest element that is within the sliding window
        myDeque = deque()

        for i in range(k):
            # For every element, the previous smaller elements are useless
            # so remove them from deque
            while myDeque and nums[myDeque[-1]] <= nums[i]:
                myDeque.pop()
            
            myDeque.append(i)

        # The element at the front of the queue is the largest element of previous window, 
        # so add it to output array
        output.append(nums[myDeque[0]])

        # process remaining elements
        for i in range(k,len(nums)):

            # Remove the elements which are out of this window
            while myDeque and myDeque[0] <= i - k:
                myDeque.popleft() # remove from front of queue
            
            # Remove elements smaller than the currently being added element
            while myDeque and nums[myDeque[-1]] <= nums[i]:
                myDeque.pop()
            
            myDeque.append(i)

            output.append(nums[myDeque[0]])
        
        return output

mySol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
output = mySol.maxSlidingWindow(nums, k)
print(output)

nums = [1]
k = 1
output = mySol.maxSlidingWindow(nums, k)
print(output)
