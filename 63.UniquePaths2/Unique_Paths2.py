def Calculate(val, board, row, col):
    try:
        return val[(row,col)]
    except:
        if board[row][col] == 1:
            val[(row,col)] = 0
            return 0
        else:
            if row == 0 or col == 0:
                if row == 0:
                    for i in range(col):
                        if board[row][i] == 1:
                            val[(row,col)] = 0
                            return 0
                    val[(row,col)] = 1
                    return 1
                else:
                    for i in range(row):
                        if board[i][col] == 1:
                            val[(row,col)] = 0
                            return 0
                    val[(row,col)] = 1
                    return 1

                val[(row,col)] = 1
                return 1
            else:
                val[(row,col)] = Calculate(val, board, row-1, col) + Calculate(val, board, row, col-1)
                return val[(row,col)]
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        val = {}
        k = Calculate(val, obstacleGrid, len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        return k