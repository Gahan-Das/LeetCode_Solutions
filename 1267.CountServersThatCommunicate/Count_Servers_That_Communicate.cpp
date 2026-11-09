#include<vector>
using namespace std;
class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int count = 0;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == 1){
                    int k = i-1;
                    bool flag = false;
                    while(k != -1){
                        if(grid[k][j] == 1){
                            flag = true;
                            count++;
                            break;
                        }
                        k--;
                    }
                    if(flag){
                        continue;
                    }
                    k = j-1;
                    while(k != -1){
                        if(grid[i][k] == 1){
                            flag = true;
                            count++;
                            break;
                        }
                        k--;
                    }
                    if(flag){
                        continue;
                    }
                    k = j+1;
                    while(k != grid[i].size()){
                        if(grid[i][k] == 1){
                            flag = true;
                            count++;
                            break;
                        }
                        k++;
                    }
                    if(flag){
                        continue;
                    }
                    k = i+1;
                    while(k != grid.size()){
                        if(grid[k][j] == 1){
                            flag = true;
                            count++;
                            break;
                        }
                        k++;
                    }
                }
            }
        }
        return count;
    }
};