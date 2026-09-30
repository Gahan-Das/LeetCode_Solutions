class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        table = [[True] * n for _ in range(n)]
        for start in range(n-1, -1, -1):
            for end in range(start+1,n):
                table[start][end] = (s[start] == s[end] and table[start+1][end-1])
        dp = [0 for _ in range(n+1)]
        # print(table)
        for cut in range(n-1, -1, -1):
            minCuts = 2000
            for part in range(cut, n):
                if table[cut][part]:
                    cuts = 1 + dp[part+1]
                    minCuts = min(minCuts, cuts)
            dp[cut] = minCuts
        return dp[0]-1
