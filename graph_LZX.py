class Solution(object):
    
    
    def __init__(self,a = 0):
        self.a = a 
    
    def dfs(self, g, r, c):
            lenr, lenc = len(g), len(g[0])
            if (r>=lenr or c>=lenc or r<0 or c<0 or g[r][c]==0):
                return
            g[r][c] = 0
            self.a += 1
            self.dfs(g, r-1, c)
            self.dfs(g, r+1, c)
            self.dfs(g, r, c-1)
            self.dfs(g, r, c+1)

    def maxAreaOfIsland(self, grid):
        self.a = 0
        if (len(grid)==0 or len(grid[0])==0 or grid==None):
            return 0
        area = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1):
                    self.dfs(grid, i, j)
                    area.append(self.a)
                    self.a = 0
        if len(area)==0:
            return 0
        return max(area)

input = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
solver = Solution()
print(solver.maxAreaOfIsland(input))

