class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        present_row = {}
        present_col = {}
        
 
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    try:
                        if board[i][j] in present_row[i]:
                            return False
                        else:
                            present_row[i] += [board[i][j]]
                    except:
                        present_row[i] = [board[i][j]]
                
                if board[j][i] != '.':
                    try:
                        if board[j][i] in present_col[i]:
                            return False
                        else:
                            present_col[i] += [board[j][i]]
                    except:
                        present_col[i] = [board[j][i]]
        iterate = [(0,3,0,3),
                   (0,3,3,6),
                   (0,3,6,9),
                   (3,6,0,3),
                   (3,6,3,6),
                   (3,6,6,9),
                   (6,9,0,3),
                   (6,9,3,6),
                   (6,9,6,9)]
        for i in iterate:
            present = []
       
            for j in range(i[0], i[1]):
                for k in range(i[2], i[3]):
                    if board[j][k] != '.':
                        if board[j][k] in present:
                            return False
                        else:
                            present += [board[j][k]]
        return True


                    




        