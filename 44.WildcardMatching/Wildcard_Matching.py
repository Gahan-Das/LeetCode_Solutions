
def isMatchRec(s, p, m, n, store):  
    if m == len(s) and n == len(p):
        store[m, n] = True
        return True
    if m > len(s) or n > len(p):
        store[m, n] = False
        return False

    try:
        if store[m, n] == True:
            return True
        else:
            return False
    except:
        pass

    try:
        if p[n] == '?':
            store[m, n] = True
            return isMatchRec(s, p, m+1, n+1, store)
        elif p[n] == '*':
            try:
                if p[n+1] == '*':
                    return isMatchRec(s, p, m, n+1, store)
            except:
                pass
            none = isMatchRec(s, p, m, n+1, store)
            one_or_more = isMatchRec(s, p, m+1, n, store)
            if none == True or one_or_more == True:
                store[m, n] = True
                return True
            else:
                store[m ,n] = False
                return False
        else:
            if p[n] == s[m]:
                store[m, n] = True
                return isMatchRec(s, p, m+1, n+1, store)
            else:
                store[m, n] = False
                return False
    except:
        store[m, n] = False
        return False

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        store = {}
        return isMatchRec(s, p, 0, 0, store)