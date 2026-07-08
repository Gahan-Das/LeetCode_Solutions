temp = []
ans = []
def combineRec(i, st,  k, n):
    global temp
    if i == k:
        global ans
        global answer
        ans += [temp[:]]
        return False
    for j in range(st, n+1):
        if j not in temp:
            temp += [j]
            if combineRec(i+1, j+1, k, n):
                return False
            temp = temp[:-1]
    return False
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        global temp
        global ans
        temp = []
        ans = []
        st = 1
        combineRec(0, st, k, n)
        return ans
