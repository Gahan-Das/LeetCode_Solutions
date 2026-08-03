class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        list = []
        for i in range(numRows):
            list1 = []
            for j in range(len(s)):
                list1 += [0]
            list.append(list1)
        strlen = len(s)
        i = 0
        str = ""
        col = numRows - 1
        if numRows == 1:
            return s
        k = 0
        while i != strlen:
            for j in range(numRows):
                if k % col == 0:
                    if i == strlen:
                        break
                    list[j][k] = s[i]
                    i = i + 1
                elif (j+k)%col == 0:
                    if i == strlen:
                        break
                    list[j][k] = s[i]
                    i = i + 1
            k = k + 1
        for i in range(numRows):
            for j in range(len(s)):
                if list[i][j] != 0:
                    str += list[i][j]
        return str
        
        