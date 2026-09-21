class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []

        depthMap = {}
        ans = []
        wordMap = set(wordList)
        depthMap[beginWord] = 0
        def dfs(word, seq):
            if word == beginWord:
                ans.append(seq[::-1])
                return
            step = depthMap[word]
            for i in range(len(word)):
                original = word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    word = word[:i] + ch + word[i+1:]
                    if word in depthMap and step == depthMap[word]+1:
                        seq.append(word)
                        dfs(word,seq)
                        seq.pop()
                word = word[:i] + original + word[i+1:]  

        queue = [beginWord]
        wordMap.discard(beginWord)
        while queue:
            word = queue.pop(0)
            step = depthMap[word]
            if word == endWord:
                break
            for i in range(len(word)):
                original = word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    word = word[:i] + ch + word[i+1:]
                    if word in wordMap:
                        depthMap[word] = step+1
                        queue.append(word)
                        wordMap.discard(word)
                word = word[:i] + original + word[i+1:]
        
        if endWord in depthMap:
            dfs(endWord, [endWord])
        return ans
    

