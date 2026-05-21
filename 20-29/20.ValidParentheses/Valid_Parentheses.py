class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0
        string = ""
        for i in range(len(s)):
            
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                count = count + 1
                string += s[i]
            elif s[i] == ')' or s[i] == '}' or s[i] == ']':
                count = count - 1
                if count < 0:
                    return False
                if s[i] == ')':
                    if string[-1] != '(':
                        return False
                    string = string[:-1]
                elif s[i] == '}':
                    if string[-1] != '{':
                        return False
                    string = string[:-1]
                elif s[i] == ']':
                    if string[-1] != '[':
                        return False
                    string = string[:-1]
        if count == 0:
            return True
        else:
            return False
                     

            


        