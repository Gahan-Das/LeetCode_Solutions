class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = ""
        carry = 0
        i = len(a)-1
        j = len(b)-1
        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                if carry:
                    s = '1' + s
                else:
                    s = '0' + s
                    carry = 1
            elif a[i] == '1' or b[j] == '1':
                if carry:
                    s = '0' + s
                else:
                    s = '1' + s
            else:
                if carry:
                    s = '1' + s
                    carry = 0
                else:
                    s = '0' + s
            i = i - 1
            j = j - 1
        while i >= 0:
            if a[i] == '1':
                if carry:
                    s = '0' + s
                else:
                    s = '1' + s
            else:
                if carry:
                    s = '1' + s
                    carry = 0
                else:
                    s = '0' + s
            i = i - 1
        while j >= 0:
            if b[j] == '1':
                if carry:
                    s = '0' + s
                else:
                    s = '1' + s
            else:
                if carry:
                    s = '1' + s
                    carry = 0
                else:
                    s = '0' + s
            j = j - 1
        if carry:
            s = '1' + s
        return s
            
 
        