def isMatchCheck(s, p, m, n):
        if n == 0:
            return m == 0
        if m == 0:
            if p[n - 1] == '*':
                return isMatchCheck(s, p, m, n-2)
            return False
        if m >= 1 and (s[m - 1] == p[n - 1] or p[n - 1] == '.'):
            return isMatchCheck(s, p, m-1, n-1)
        if p[n - 1] == '*':
            if n >= 2: 
                zero = isMatchCheck(s, p, m, n-2)
                one_or_more = False
            if p[n - 2] == s[m - 1] or p[n - 2] == '.':
                one_or_more = isMatchCheck(s, p, m-1, n)
            return zero or one_or_more
        return False
class Solution(object):
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return isMatchCheck(s, p, len(s), len(p))
    