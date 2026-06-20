
store = {}
def permutationGenerate(n, final, k, opt):
    if len(k) == n:
        final.append(''.join(map(str, k)))
        return False
    for i in range(1,n+1):
        if not (opt & (1 << i-1)):
            if permutationGenerate(n, final, k+[i], opt | (1 << i-1)):
                return False
    return False
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        final = []
        l = []
        m = 0
        opt = 0*n

        try:
            return store[n][k-1]
        except:
            permutationGenerate(n, final, l, opt)
            store[n] = final
            return final[k-1]
