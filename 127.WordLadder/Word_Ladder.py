class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        length = len(beginWord)
        depthMap = {}
        depthMap[beginWord] = 1
        queue = [beginWord]
        wordSet = set(wordList)
        wordSet.add(beginWord)

        while queue:
            word = queue.pop(0)
            step = depthMap[word]
            if word == endWord:
                break
            for i in range(length):
                original = word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    word = word[:i] + ch + word[i+1:]
                    if word in wordSet:
                        depthMap[word] = step+1
                        queue.append(word)
                        wordSet.discard(word)
                word = word[:i] + original + word[i+1:]
        
        if endWord in depthMap:
            return depthMap[endWord]
        else:
            return 0