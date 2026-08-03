class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []
        ans = []

        for i in range(1,len(s)-2):
            for j in range(i+1, len(s)-1):
                for k in range(j+1, len(s)):
                    if len(s[:i]) > 3 or len(s[i:j]) > 3 or len(s[j:k]) > 3 or len(s[k:]) > 3:
                        continue
                    if int(s[:i]) > 255 or int(s[i:j]) > 255 or int(s[j:k]) > 255 or int(s[k:]) > 255:
                        continue 
                    if len(s[k:]) > 1:
                        if s[k] == '0':
                            continue
                    if len(s[j:k]) > 1:
                        if s[j] == '0':
                            continue
                    if len(s[i:j]) > 1:
                        if s[i] == '0':
                            continue
                    if len(s[:i]) > 1:   
                        if s[0] == '0':
                            continue
                    ans += [s[:i]+'.'+s[i:j]+'.'+s[j:k]+'.'+s[k:]]
        return ans