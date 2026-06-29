int uniquePaths(int m, int n) {
    if(m == 1 || n == 1){
        return 1;
    }
    unsigned long long int board[101][101];
    for(int i = 1; i <= m; i++){
        board[i][0] = 0;
        board[i][1] = 1;
    }
    for(int i = 1; i <= n; i++){
        board[1][i] = 1;
        board[0][i] = 0;
    }
    int sj = 2, si = 3, i = 1, j = 1;
    do{
        i++;
        j--;
        if(i > m || j < 1){ 
            if(sj <= n){
                i = 2;
                j = sj++;
            }
            else{
                i = si++;
                j = n;
            }
        }
        board[i][j] = board[i-1][j] + board[i][j-1];
    }while(i != m || j != n);
    return board[m][n];
}