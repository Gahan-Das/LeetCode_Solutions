class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        ans = {}
        ans[-1] = 1
        start = 0
        for i in range(len(s)):
            if s[i] == '1' or s[i] == '2':
                start += 1
                if start == 1 or start == 2:
                    ans[i] = ans[i-start] * start
                else:
                    ans[i] = ans[i-start] * self.fib(start)
            elif s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    ans[i] = ans[i-2]
                    start = 0
                else:
                    return 0
            else:
                if i == 0:
                    ans[i] = 1
                else:
                    if int(s[i-1]+s[i]) <= 26:
                        start += 1
                        ans[i] = ans[i-start] * self.fib(start)
                    else:
                        ans[i] = ans[i-1] 
                    start = 0
        return ans[len(s)-1]         
    def fib(self, start):
        try:
            return val[start+1]
        except:
            pass
        val = {}
        val[0] = 0
        val[1] = 1
        for i in range(2,start+2):
            val[i] = val[i-1] + val[i-2]
        return val[start+1]
        

        