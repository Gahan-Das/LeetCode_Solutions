#include<vector>
using namespace std;
class Solution {
public:
    void reach(vector<vector<char>>& board, int i, int j, vector<vector<int>>& flag){
        int rowLen = board.size();
        int colLen = board[0].size();
        if(flag[i][j] == 1){
            return;
        }
        flag[i][j] = 1;
        if(i != 0){
            if(board[i-1][j] == 'O'){
                reach(board, i-1, j, flag);
            }
        }
        if(i != rowLen-1){
            if(board[i+1][j] == 'O'){
                reach(board, i+1, j, flag);
            }
        }
        if(j != 0){
            if(board[i][j-1] == 'O'){
                reach(board, i, j-1, flag);
            }
        }
        if(j != colLen-1){
            if(board[i][j+1] == 'O'){
                reach(board, i, j+1, flag);
            }
        }
    }
    void solve(vector<vector<char>>& board) {
        int rowLen = board.size();
        int colLen = board[0].size();
        int i, j;
        vector<vector<int>> flag(rowLen, vector<int>(colLen, 0));
        i = 0;
        for(j = 0; j < colLen; j++){
            if(board[i][j] == 'O'){
                reach(board, i, j, flag);
            }
        }
        i = rowLen-1;
        for(j = 0; j < colLen; j++){
            if(board[i][j] == 'O'){
                reach(board, i, j, flag);
            }
        }
        j = 0;
        for(i = 0; i < rowLen; i++){
            if(board[i][j] == 'O'){
                reach(board, i, j, flag);
            }
        }
        j = colLen-1;
        for(i = 0; i < rowLen; i++){
            if(board[i][j] == 'O'){
                reach(board, i, j, flag);
            }
        }
        for(i = 0; i < rowLen; i++){
            for(j = 0; j < colLen; j++){
                if(board[i][j] == 'O' && flag[i][j] == 0){
                    board[i][j] = 'X';
                }
            }
        }
    }
};