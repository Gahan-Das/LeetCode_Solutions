#include<vector>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& arr) {
        int n = arr.size();
        int mini = arr[0];
        vector<int> d1(n,0);
        int ans = 0;
        for(int i = 1; i < n; i++){
            mini = min(mini, arr[i]);
            ans = max(ans, arr[i]-mini);
            d1[i] = ans;
        }
        vector<int> d2(n,0);
        int maxi = arr[n-1];
        ans = 0;
        for(int i = n-2; i>= 0; i--){
            maxi = max(maxi, arr[i]);
            ans = max(ans, maxi-arr[i]);
            d2[i] = ans;
        }
        ans = 0;
        for(int i = 0; i < n-1; i++){
            ans = max(ans, d1[i]+d2[i+1]);
        }
        ans = max(ans, max(d1[n-1],d2[0]));
        return ans;
    }
};