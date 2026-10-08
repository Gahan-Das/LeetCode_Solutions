#include<vector>
using namespace std;
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        if(n == 1 && gas[0] >= cost[0]){
            return 0;
        }
        int tank = 0;
        for(int i = 0; i < n; i++){
            if(gas[i] <= cost[i]){
                continue;
            }
            tank = gas[i]-cost[i];
            int j = i+1;
            while(tank >= 0){
                if(j == n){
                    j = 0;
                }
                if(j == i){
                    return j;
                }
                tank += gas[j]-cost[j];
                j++;
                
            }
        }
        return -1;
    }
};