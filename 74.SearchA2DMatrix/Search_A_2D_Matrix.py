class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowSize = len(matrix)
        colSize = len(matrix[0])
        l = 0
        r = rowSize-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        idx = r
        l = 1
        r = colSize-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[idx][mid] == target:
                return True
            elif matrix[idx][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
