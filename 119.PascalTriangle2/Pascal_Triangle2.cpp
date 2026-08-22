#include<vector>
using namespace std;
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> answer;
        for(int i = 0; i <= rowIndex; i++){
            if(i <= 1){
                answer.push_back(1);
            } else {
                vector<int> temp;
                temp.push_back(1);
                for(int j = 1; j < i; j++){
                    temp.push_back(answer[j] + answer[j-1]);
                }
                answer = temp;
                answer.push_back(1);
            }
        }
        return answer;
    }
};