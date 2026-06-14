class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1
        ans = []
        limit = (bottom+1)*(right+1)
        while left < right and top < bottom:
            i = left
            while i != right+1:
                print(left, i)
                ans += [matrix[left][i]]
                if len(ans) == limit:
                    break
                i = i + 1
            top = top + 1
            i = top
            while i != bottom+1:
                print(i, right)
                ans += [matrix[i][right]]
                if len(ans) == limit:
                    break
                i = i + 1
            right = right - 1
            i = right
            while i != left-1:
                print(bottom, i)
                ans += [matrix[bottom][i]]
                if len(ans) == limit:
                    break
                i = i - 1
            bottom = bottom - 1
            i = bottom
            while i != top-1:
                print(i, left)
                ans += [matrix[i][left]]
                if len(ans) == limit:
                    break
                i = i - 1
            left = left + 1
        if len(ans) != limit:
            i = left
            while i != right+1:
                    print(left, i)
                    ans += [matrix[left][i]]
                    if len(ans) == limit:
                        break
                    i = i + 1
            top = top + 1
        if len(ans) != limit:
            i = top
            while i != bottom+1:
                    print(i, right)
                    ans += [matrix[i][right]]
                    if len(ans) == limit:
                        break
                    i = i + 1
        return ans
