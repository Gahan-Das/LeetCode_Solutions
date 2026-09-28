#include<vector>
#include<unordered_map>
using namespace std;
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        unordered_map<int,int> map;
        map[0] = 0;
        for(int i = 0; i < triangle.size(); i++){
            unordered_map<int,int> temp;
            for(int j = 0; j <= i; j++){
                if(j == 0){
                    temp[j] = map[j] + triangle[i][j];
                } else if(j == i){
                    temp[j] = map[j-1] + triangle[i][j];
                } else {
                    temp[j] = min(map[j], map[j-1]) + triangle[i][j];
                }
            }
            map = temp;
        }
        int leastCost = map[0];
        for(int i = 1; i < triangle.size(); i++){
            if(map[i] < leastCost){
                leastCost = map[i];
            }
        }
        return leastCost;
    }
};