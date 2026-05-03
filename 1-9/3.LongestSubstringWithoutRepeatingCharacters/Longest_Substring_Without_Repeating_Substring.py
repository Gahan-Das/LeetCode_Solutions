class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        max_count = 0
        str = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in str:
                    str += s[j]
                    count = count + 1
                else:
                    if max_count < count:
                        max_count = count
                    count = 0
                    str = ""
                    break
        if max_count < count:
            max_count = count
        return max_count
        