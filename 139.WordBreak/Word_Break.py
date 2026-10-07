class Solution(object):
    table = {}
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        global table
        table = {}
        tmp = {}
        for key in wordDict:
            tmp[key] = 1
        wordDict = tmp
        i = 0
        t = self.word(s, i, len(s), wordDict)
        return t
    def word(self, s, i, j, wordDict):
        global table
        if i == j:
            return True
        table[0] = True
        for it in range(1,j+1):
            for check in range(it):
                if table[check] == True:
                    if s[check:it] in wordDict:
                        table[it] = True
            try:
                table[it]
            except:
                table[it] = False
                
        if table[j] == True:
            return True
        return False