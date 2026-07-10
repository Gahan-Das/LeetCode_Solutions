visited  = []
def checkExist(board, i, j, word):
    global visited
    if len(word) == 0:
        return True
    visited += [(i,j)]
    if i-1 >= 0 and board[i-1][j] == word[0] and (i-1,j) not in visited:
        opt1 = checkExist(board, i-1, j, word[1:])
        if opt1:
            return True
    if j+1 < len(board[0]) and board[i][j+1] == word[0] and (i,j+1) not in visited:
        opt2 = checkExist(board, i, j+1, word[1:])
        if opt2:
            return True
    if i+1 < len(board) and board[i+1][j] == word[0] and (i+1,j) not in visited:
        opt3 = checkExist(board, i+1, j, word[1:])
        if opt3:
            return True
    if j-1 >= 0 and board[i][j-1] == word[0] and (i,j-1) not in visited:
        opt4 = checkExist(board, i, j-1, word[1:])
        if opt4:
            return True
    visited = visited[:-1]
    return False
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        global visited 
        row = len(board)
        col = len(board[0])
        ans = False
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    visited = []
                    ans = checkExist(board, i, j, word[1:])
                    if ans:
                        return True
        return ans