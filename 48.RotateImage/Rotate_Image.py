import copy
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        cpy = copy.deepcopy(matrix)
        sz = len(matrix)
        for i in range(sz):
            for j in range(sz):
                matrix[j][sz-i-1] = cpy[i][j]

                
