class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ans = ""
        string = path.split('/')
    
        temp = ""
        store = []
        for i in range(len(string)):
            if string[i] == '..':
                try:
                    ans = store[-1]
                    store = store[:-1]
                except:
                    ans = ''
                continue
            count = 1
            if string[i] == '.' or string[i] == '':
                continue
            store += [ans]
            ans += '/' + string[i]
        if ans == '':
            ans += '/'
        return ans
            


        