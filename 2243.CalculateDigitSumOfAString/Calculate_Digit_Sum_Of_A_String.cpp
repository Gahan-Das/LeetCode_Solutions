#include<string>
using namespace std;
class Solution {
public:
    string digitSum(string s, int k) {
        if(s.size() <= k){
            return s;
        }
        int curr = 0,i;
        string str = "";
        for(i = 0; i < s.size(); i++){
            if(i % k == 0 && i != 0){
                str += to_string(curr);
                curr = 0;
            }
            curr += s[i] - '0';
        }
        str += to_string(curr);
        if(str.size() > k){
            return digitSum(str, k);
        }
        else{
            return str;
        }
    }
};