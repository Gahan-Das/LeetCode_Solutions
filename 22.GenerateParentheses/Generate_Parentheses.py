def validParentheses(val):
    count = 0

    for i in range(len(val)):
        if count < 0:
            return False
        if val[i] == "(":
            count = count + 1
        else:
            count = count - 1
            
    if count == 0:
        return True
    else:
        return False


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = {}
        output = []
        
        for i in range(2*n):
            if i == 0:
                out[1] = ['(']
                continue
            for j in out[i]:
                try:    
                    out[i+1] += [ j+'(' ]
                    out[i+1] += [ j+')' ]
                except:
                    out[i+1] = [ j+'(' ]
                    out[i+1] += [ j+')' ]
     
        for i in out[2*n]:
            if validParentheses(i) == True:
                output += [i]
        return output
            

        