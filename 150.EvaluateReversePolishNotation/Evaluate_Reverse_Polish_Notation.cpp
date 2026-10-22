#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> ans;
        for(int i = 0; i < tokens.size(); i++){

            if(tokens[i] == "+"){
                int val1 = ans.back();
                ans.pop_back();
                int val2 = ans.back();
                ans.pop_back();
                ans.push_back(val1+val2);
            }
            else if(tokens[i] == "-"){
                int val1 = ans.back();
                ans.pop_back();
                int val2 = ans.back();
                ans.pop_back();
                ans.push_back(val2-val1);
            }
            else if(tokens[i] == "*"){
                int val1 = ans.back();
                ans.pop_back();
                int val2 = ans.back();
                ans.pop_back();                
                ans.push_back(val1*val2);
            }
            else if(tokens[i] == "/"){
                int val1 = ans.back();
                ans.pop_back();
                int val2 = ans.back();
                ans.pop_back();
                ans.push_back(val2/val1);
            } 
            else{
                ans.push_back(stoi(tokens[i]));
            }
        }
        return ans.back();
    }
};