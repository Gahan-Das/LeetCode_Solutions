class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowSize = len(matrix)
        colSize = len(matrix[0])
        rowZero = []
        colZero = []
        for i in range(rowSize):
            for j in range(colSize):
                if matrix[i][j] == 0:
                    rowZero += [i]
                    colZero += [j]
        temp = []
        for k in range(colSize):
            temp += [0]
        for i in rowZero:
            matrix[i] = temp
        for i in range(rowSize):
            for j in colZero:
                matrix[i][j] = 0