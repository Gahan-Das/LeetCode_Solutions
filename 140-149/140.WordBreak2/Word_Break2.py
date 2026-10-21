class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        table = {}
        string = {}
        table[0] = True
        string[0] = ['']

        wordDict = set(wordDict)
        for i in range(1,len(s)+1):
            string[i] = ['']
            for j in range(i):
                if table[j] == True:
                    if s[j:i] in wordDict:
                        if string[i]==['']:
                            string[i] = [string[j][k] + ' ' + s[j:i] for k in range(len(string[j]))] 
                        else:   
                            string[i] += [string[j][k] + ' ' + s[j:i] for k in range(len(string[j]))]
                        table[i] = True
            try:
                table[i]
            except:
                table[i] = False
        for i in range(len(string[len(s)])):
            string[len(s)][i] = string[len(s)][i][1:]
        if string[len(s)] == [""]:
            return []
        return string[len(s)]