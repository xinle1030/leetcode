from typing import List

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        if not grid:
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        
        return count
                

    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len((grid[i])) or grid[i][j] != "1":
            return
        grid[i][j] = "-"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)