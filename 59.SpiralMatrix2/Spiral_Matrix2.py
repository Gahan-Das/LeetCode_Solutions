class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(n):
            ans += [[]]
        top = 0
        bottom = n-1
        left = 0
        right = n-1
        k = 1
        while k <= n**2:
            i = left
            while i <= right:
                ans[top] = ans[top][:i] + [k] + ans[top][i:]
                k = k + 1
                i = i + 1
            top = top+1
            i = top
            while i <= bottom:
                ans[i] = ans[i][:left] + [k] + ans[i][left:]
                k = k + 1
                i = i + 1
            right = right - 1
            i = right
            while i >= left:
                ans[bottom] = ans[bottom][:left] + [k] + ans[bottom][left:]
                k = k + 1
                i = i - 1
            bottom = bottom - 1
            i = bottom
            while i >= top:
                ans[i] = ans[i][:left] + [k] + ans[i][left:]
                k = k + 1
                i = i - 1
            left = left + 1

        return ans