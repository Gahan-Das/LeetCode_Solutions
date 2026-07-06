
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        
        countT = {}
        window = {}

        for i in t:
            try:
                countT[i] += 1
            except:
                countT[i] = 1
        
        have = 0
        need = len(countT)
        l = 0
        r = 0
        res = []
        resLen = 10**7

        while r < len(s) and l <= len(s):
            if have != need:
                try:
                    window[s[r]] += 1
                except:
                    window[s[r]] = 1

                try:
                    if window[s[r]]-1 < countT[s[r]]:
                        if window[s[r]] >= countT[s[r]]:
                            have += 1
                except:
                    pass

            else:
                window[s[l-1]] -= 1

                try:
                    if window[s[l-1]] >= countT[s[l-1]]:
                        pass
                    else:
                        have -= 1
                except:
                    pass

            if have == need:
                if r-l+1 < resLen:
                    res = [l,r]
                    resLen = r-l+1
                l += 1
            else:
                r += 1

        if res != []:
            return s[res[0]:res[1]+1]
        else:
            return ""
            