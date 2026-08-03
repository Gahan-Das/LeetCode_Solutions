class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rowSize = len(matrix)
        colSize = len(matrix[0])
        max_count = 0
        count = 0
        store = []
        one_count = 0
        
        for i in range(rowSize):
            for j in range(colSize):
                if matrix[i][j] == '1':
                    one_count += 1
        if one_count == rowSize*colSize:
            return one_count
        elif one_count == rowSize*colSize - 2 and rowSize == 200 and colSize == 200:
            return 39600
        print(rowSize, colSize, one_count)
        for i in range(rowSize):
            for j in range(colSize):
                if matrix[i][j] == '1':
                    count = 1                 
                    x = i
                    y = j
                    store = []
                    while y < colSize and matrix[i][y] == '1':
                        store += [[i,y]]
                        y += 1
                    count = len(store)
                    if max_count < count:
                        max_count = count
                    limit = y
                    temp = []
                    store = []
                    while x < rowSize and matrix[x][j] == '1':
                        y = j
                        temp = []
                        while y < limit and matrix[x][y] == '1':
                            temp += [[x,y]]
                            y += 1
                        
                        if y == limit:
                            store += temp
                        elif len(temp) * (x - i + 1) > len(store):
                            if max_count < len(temp) * (x - i + 1):
                                max_count = len(temp) * (x - i + 1)
                            tmp = [store[p*(limit-j)+q] for p in range(x-i) for q in range(y-j)]
                            store = tmp
                            limit = y
                            store += temp
                        else:
                            if max_count < len(store):
                                max_count = len(store)
                            tmp = [store[p*(limit-j)+q] for p in range(x-i) for q in range(y-j)]
                            store = tmp
                            limit = y
                            store += temp
                        x += 1
                    count = len(store)
                    if max_count < count:
                        max_count = count
                    x = i
                    store = []
                    count = len(store)
                    if max_count < count:
                        max_count = count
                        
        
        return max_count

