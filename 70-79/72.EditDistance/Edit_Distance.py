
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        table = {}
        table[0,0] = 0
        for i in range(-1,len(word2)):
            table[-1,i] = i+1
        for i in range(-1,len(word1)):
            table[i,-1] = i+1
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    add = 0
                else:
                    add = 1
                table[i,j] = min(table[i-1,j] + 1,
                                 table[i,j-1] + 1,
                                 table[i-1,j-1] + add)
                    
        return table[len(word1)-1,len(word2)-1] 


