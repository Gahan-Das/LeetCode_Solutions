class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == 'e' or s== 'E' or s == '.' or s == '-' or s == '+':
            return False
        for i in ['-.e', '+.e', '-.E', '+.E', '..', '...', '....']:
            if i in s:
                return False
        if 'e' in s or 'E' in s:
            if 'e' in s:
                whole = s.split('e')
            else:
                whole = s.split('E')
            if len(whole) > 2:
                return False
            if len(whole[0]) == 0 or len(whole[1]) == 0:
                return False
            if len(whole[0]) == 1 and (whole[0][0] == '-' or whole[0][0] == '+'):
                return False
            if '.' in whole[0]:
                part = whole[0].split('.')
                if len(part[0]) == 0 and len(part[1]) == 0:
                    return False
            sign = 0
            for i in range(len(whole[0])):
                if whole[0][i] == '-' or whole[0][i] == '+':
                    sign = i
                if whole[0][i] not in "0123456789eE+-.":
                    return False
            if sign != 0:
                return False
            if '.' in whole[1]:
                return False
            
            if len(whole[1]) == 1 and (whole[1][0] == '-' or whole[1][0] == '+'):
                return False
            sign = 0
            for i in range(len(whole[1])):
                if whole[1][i] == '-' or whole[1][i] == '+':
                    sign = i
                if whole[1][i] not in "0123456789+-":
                    return False
            if sign != 0:
                return False
                    
            return True
        else:
            if '.' in s:
                whole = s.split('.')
                if len(whole) > 2:
                    return False
                if len(whole[0]) == 1 and (whole[0][0] == '-' or whole[0][0] == '+'):
                    if len(whole[1]) == 0:
                        return False
                
                sign = 0
                for i in range(len(s)):
                    if s[i] == '-' or s[i] == '+':
                        sign = i
                if sign != 0:
                    return False
                try:
                    for i in range(len(whole[0])):
                        if whole[0][i] not in "0123456789eE+-.":
                            return False
                except:
                    pass
                try:
                    for i in range(len(whole[1])):
                        if whole[1][i] not in "0123456789eE+-.":
                            return False
                except:
                    pass
                return True
            else:
                sign = 0
                for i in range(len(s)):
                    if s[i] == '-' or s[i] == '+':
                        sign = i
                if sign != 0:
                    return False
                for i in range(len(s)):
                    if s[i] not in "0123456789+-":
                        return False
                return True

                    


        