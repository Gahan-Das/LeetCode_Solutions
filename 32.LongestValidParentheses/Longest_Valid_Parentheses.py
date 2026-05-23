def validParentheses(s):
    
    if s[0] == ')':
        return 0
    else:
        count = 1
        max_val = 0
        for i in range(1, len(s)):
            if count < 0:
                return i-1
            if count == 0:
                if i > max_val:
                    max_val = i
            if s[i] == '(':
                count = count + 1
            elif s[i] == ')':
                count = count - 1
        if count == 0:
            return len(s)
        else:
            return max_val
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                continue
            flag = 0
        if flag:
            return 0
        store = []
        for i in range(len(s)):
            temp = validParentheses(s[i:])
            store += [temp]
  

        try:
            return max(store)
        except Exception as e:
            return 0
