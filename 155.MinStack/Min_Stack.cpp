#include<vector>
using namespace std;
class MinStack {
public:
    vector<pair<int, int>> arr;
    MinStack() {
        arr.clear();
    }
    
    void push(int value) {
        if(arr.empty()){
            arr.push_back({value, value});
        }
        else{
            auto temp = arr.back();
            int min = temp.second;
            if(value < min){
                arr.push_back({value, value});
            }
            else{
                arr.push_back({value, min});
            }
        }
    }
    
    void pop() {
        arr.pop_back();
    }
    
    int top() {
        auto temp = arr.back();
        return temp.first;
    }
    
    int getMin() {
        auto temp = arr.back();
        return temp.second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */