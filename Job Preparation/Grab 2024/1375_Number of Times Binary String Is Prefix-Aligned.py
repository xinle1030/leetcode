from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = 0
        right = 0
        
        for i in range(len(flips)):
            right = max(right, flips[i])
            # Check if right equals i + 1. If it does, it means that all the bits up to index i are flipped (since the indices are 1-indexed). 
            # Increment the result counter res.
            if right == i + 1:
                res += 1
                
        return res

mySol = Solution()
flips = [3,2,4,1,5]
print(mySol.numTimesAllBlue(flips))

# flips = [4,1,2,3]
# print(mySol.numTimesAllBlue(flips))