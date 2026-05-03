class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        final_str = ""
        for i in range(len(s)):
            str = ""
            for j in range(i,len(s)):
                str = s[i:j+1]
                if str == str[::-1]:
                    if len(final_str) < len(str):
                        final_str = str
        return final_str