class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.total = 0
        empty = 1
        m, n = len(grid), len(grid[0])        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: empty += 1
                elif grid[i][j] == 1: x, y = (i, j)
                elif grid[i][j] == 2: self.end = (i, j)
                    
        self.dfs(grid, x, y, empty)        
        return self.total
    
    def dfs(self, grid, x, y, empty):
        if not (x in range(len(grid)) and y in range(len(grid[0])) and grid[x][y] >= 0):
            return        
        if (x,y) == self.end:
            if empty == 0:
                self.total += 1
            return        
        grid[x][y] = -2        
        self.dfs(grid, x - 1, y, empty - 1)
        self.dfs(grid, x + 1, y, empty - 1)
        self.dfs(grid, x, y - 1, empty - 1)
        self.dfs(grid, x, y + 1, empty - 1)        
        grid[x][y] = 0