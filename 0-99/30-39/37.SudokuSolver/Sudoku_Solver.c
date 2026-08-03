#include<stdbool.h>
bool isSafe(char** board, int row, int col, int num){
    char no = num+'0';
    for(int i = 0; i < 9; i++){
        if(board[row][i] == no){
            return false;
        }
    }
    for(int i = 0; i < 9; i++){
        if(board[i][col] == no){
            return false;
        }
    }
    int startRow = row - (row%3);
    int startCol = col - (col%3);
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(board[i+startRow][j+startCol] == no){
                return false;
            }
        }
    }
    return true;
}
bool solveSudokuRec(char** board, int row, int col){
    if (row == 8 && col == 9){
        return true;
    }
    if(col == 9){
        row += 1;
        col = 0;
    }
    if (board[row][col] != '.'){
        return solveSudokuRec(board, row, col+1);
    }
    for(int i = 1; i <= 9; i++){
        if (isSafe(board, row, col, i)){
            char tmp = i + '0';
            board[row][col] = tmp;
            if(solveSudokuRec(board, row, col+1)){
                return true;
            }
            board[row][col] = '.';
        }
    }
    return false;
}
void solveSudoku(char** board, int boardSize, int* boardColSize) {
    solveSudokuRec(board, 0, 0);
}