class Solution(object):
    ans = []
    def isPalindrome(self, s):
        if s == "":
            return False
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True 
    def part(self, s, temp):
        global ans
        print(temp)
        for i in range(1,len(s)+1):
            if self.isPalindrome(s[:i]):
                self.part(s[i:], temp+[s[:i]]) 
                if s[i:] == '':
                    temp += [s[:i]]
                    ans += [temp]
                     
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        global ans
        ans = []
        temp = []
        self.part(s, temp)
        return ans