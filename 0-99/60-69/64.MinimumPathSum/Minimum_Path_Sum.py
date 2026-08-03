class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        val = {}
        val[0,0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    val[i,j] = val[i,j-1] + grid[i][j]
                elif j == 0:
                    val[i,j] = val[i-1,j] + grid[i][j]
                else:
                    if val[i-1,j] + grid[i][j] < val[i,j-1] + grid[i][j]:
                        val[i,j] = val[i-1,j] + grid[i][j]
                    else:
                        val[i,j] = val[i,j-1] + grid[i][j]
        return val[len(grid)-1,len(grid[0])-1]
        