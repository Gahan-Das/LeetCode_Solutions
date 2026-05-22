class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        leng = len(words)
        length = len(words[0])
        i = 0
        ret = []
        while i < len(s):
            k = i + leng*length
            temp = s[i:k]
            window = [temp[j:j+length] for j in range(0, len(temp), length)]
            if sorted(window) == sorted(words):
                ret += [i]
            
            i = i + 1
        return ret

