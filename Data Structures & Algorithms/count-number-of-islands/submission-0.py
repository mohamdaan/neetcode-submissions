class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #island is connected 1s either left or right of current index or up or down 
        # start with current index and breadthsearch up down left right when possible  for islands 
        ## base case will be if we go out of bounds
        ##start from top right and keep a count 
        rows = len(grid)
        cols = len(grid[0])
        count = 0 
        for r in range(0,rows):
            for c in range(0,cols):
                if (grid[r][c] == "1"):
                    count +=1
                    self.dfs(r,c,grid)
        return count


    def dfs(self,r,c,grid):
        rows = len(grid)
        cols = len(grid[0])

        if (r < 0 or c<0 or r >= rows or c >= cols or grid[r][c] == "0"):
            return
        else:
            grid[r][c] = "0"
            self.dfs(r+1,c,grid)
            self.dfs(r-1,c,grid)
            self.dfs(r,c+1,grid)
            self.dfs(r,c-1,grid)

