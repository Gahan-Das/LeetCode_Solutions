class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        table = {}
        for i in range(-1,len(t)):
            table[(i, -1)] = 0
        for j in range(-1,len(s)):
            table[(-1, j)] = 1
        for i in range(len(t)):
            for j in range(len(s)):
                if s[j] == t[i]:
                    table[(i, j)] = table[(i, j-1)] + table[(i-1, j-1)]
                else:
                    table[(i, j)] = table[(i, j-1)]
        return table[(len(t)-1,len(s)-1)]

            
        