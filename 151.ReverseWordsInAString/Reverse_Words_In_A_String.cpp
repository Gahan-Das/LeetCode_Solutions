#include<iostream>
using namespace std;
class Solution {
public:
    string reverseWords(string s) {
        int size = s.size();
        string ans = "";
        string temp = "";
        int count = 0;
        for(int i = size-1; i >= 0; i--){
            if(s[i] == ' '){
                if(temp == ""){
                    continue;
                }
                if(count == 0){
                    ans += temp;
                    count = 1;
                }
                else{
                    ans += ' ';
                    ans += temp;
                }
                temp = "";
                continue;
            }
            temp = s[i] + temp; 
        }
        if(temp != "" && count == 1){
            ans += ' ';
            ans += temp;
        } else if(temp != "" && count == 0){
            ans += temp;
        }
        return ans;
    }
};