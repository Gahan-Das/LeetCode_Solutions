val = [1,1]
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        global val
        try:
            return val[n]
        except:
            for i in range(2, 46):
                val += [val[i-1] + val[i-2]]
            return val[n]