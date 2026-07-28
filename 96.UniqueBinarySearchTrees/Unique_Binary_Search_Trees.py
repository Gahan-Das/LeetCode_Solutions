class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fact(2*n) // (self.fact(n+1)*self.fact(n))
    def fact(self, n):
        val = 1
        for i in range(1,n+1):
            val *= i
        return val