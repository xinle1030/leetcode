"""
References:

https://medium.com/@bsinghrathore32/leetcode-403-frog-jump-2561e704c4b6
https://www.youtube.com/watch?v=3FYCPlIx3YA
"""

from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for i in range(len(stones)):
            # current step
            for k in dp[stones[i]]:
                # get the possible next steps
                for step in range(k - 1, k + 2):
                    # jump to next index with the new next steps
                    if step and stones[i] + step in dp:
                        dp[stones[i] + step].add(step)
        
        # check if can pass by last stone
        return len(dp[stones[-1]]) > 0

mySol = Solution()
stones = [0,1,3,5,6,8,12,17]
print(mySol.canCross(stones))

stones = [0,1,2,3,4,8,9,11]
print(mySol.canCross(stones))