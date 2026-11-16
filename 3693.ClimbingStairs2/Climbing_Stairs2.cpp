#include<vector>
#include<limits.h>
using namespace std;
class Solution {
public:
    int climbStairs(int n, vector<int>& costs) {
        vector<int> store;
        for(int i = 0; i <= n; i++){
            store.push_back(INT_MAX);
        }
        store[0] = 0;
        for(int i = 1; i <= n; i++){
            if(i-1 >= 0){
                store[i] = min(store[i-1] + costs[i-1] + 1,store[i]);
            }
            if(i-2 >= 0){
                store[i] = min(store[i-2] + costs[i-1] + 4, store[i]);
            }
            if(i-3 >= 0){
                store[i] = min(store[i-3] + costs[i-1] + 9, store[i]);
            }
        }
        return store[n];
    }
};