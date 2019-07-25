from typing import List

class Solution:
     def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        grid = list(map(lambda col: list(map(int, col)), grid)) 
        #[[int(x) for x in rows] for rows in grid]

        def dfs(grid, i, j):
            if i == -1 or j == -1 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0:
                return
            if grid[i][j] == 1:
                grid[i][j] = 0
            dfs(grid, i, j+1)
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(grid, i, j)
                    count += 1
        return count