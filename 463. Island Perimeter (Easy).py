class Solution:
    def islandPerimeter(self, grid):
        per = 0
        for i in range(0, len(grid) ):            
            for j in range(0, len(grid[i])):
                if (grid[i][j]):
                    sides = 0       
                    if (i > 0 and grid[i - 1][j]): 
                        sides += 1 

                    if (j > 0 and grid[i][j - 1]): 
                        sides += 1

                    if (i < len(grid) - 1 and grid[i + 1][j]): 
                        sides += 1

                    if (j < len(grid[i]) - 1 and grid[i][j + 1]): 
                        sides += 1
                    
                    per += (4 - sides)
            
        return per
                 
                    
        
        