def isSafe( row, col, nesw, nwse, i, j):

    if row[i] == 0 and col[j] == 0 and nesw[i+j] == 0 and nwse[j-i] == 0:
        return True
    return False

def solveNQueensRec(row, col, nesw, nwse, final, board, n, i):

    for j in range(n):
        if isSafe(row, col, nesw, nwse, i, j):
            row[i] = 1
            col[j] = 1
            nesw[i+j] = 1
            nwse[j-i] = 1
            board[i,j] = 1

            if i == n-1:
                temp = []
                for k in range(n):
                    tmp = ""
                    for l in range(n):
                        try:
                            if board[k,l] == 1:
                                tmp += 'Q'
                            else:
                                tmp += '.'
                        except:
                            tmp += '.'
                    
                    temp += [tmp,]
                if temp not in final:
                    final += [temp]
                    row[i] = 0
                    col[j] = 0
                    nesw[i+j] = 0
                    nwse[j-i] = 0
                    board[i,j] = 0
                    return False
                return True
            if solveNQueensRec(row, col, nesw, nwse, final, board, n, i+1):
                return True
            row[i] = 0
            col[j] = 0
            nesw[i+j] = 0
            nwse[j-i] = 0
            board[i,j] = 0

    return False
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        row = {}
        col = {}
        ne_to_sw = {}
        nw_to_se = {}
        board = {}
        for i in range(n):
            row[i] = 0
            col[i] = 0
        for i in range(n):
            for j in range(n):
                nw_to_se[j-i] = 0
                ne_to_sw[i+j] = 0
                board[i,j] = 0
        final = []
        solveNQueensRec(row, col, ne_to_sw, nw_to_se, final, board, n, 0)
        return final