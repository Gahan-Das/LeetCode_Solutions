
def Func(s1, s2,store):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    try:
        return store[s1+'#'+s2]
    except:
        pass
    for i in range(1,len(s1)):
        if (Func(s1[:i],s2[:i],store) and Func(s1[i:],s2[i:],store)):
            store[s1+'#'+s2] = True
            return True
        if (Func(s1[:i],s2[-i:],store) and Func(s2[:len(s2)-i],s1[i:],store)):
            store[s1+'#'+s2] = True
            return True
    store[s1+'#'+s2] = False
    return False

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        
        store = {}
        Func(s1,s2,store)
        return store[s1+'#'+s2]
