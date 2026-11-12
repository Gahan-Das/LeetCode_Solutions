#include<stdbool.h>
int longestMonotonicSubarray(int* nums, int numsSize) {
    int maxCount = 1; // Initialize maximum count
    int count = 1; // Initialize count
    bool flag = true; // flag determines increasing or decreasing direction : true - increasing, false - decreasing
    for(int i = 1; i < numsSize; i++){ // Iterate through the loop
        if(nums[i] > nums[i-1]){ // If current value is strictly greater than the previous value then update count according to flag direction and update flag direction
            if(flag){
                count++;
            }  
            else{
                count = 2;
            }
            flag = true; 
        }
        else if(nums[i] < nums[i-1]){ // If current value is strictly lesser than the previous value then update count according to flag direction and update flag direction
            if(!flag){
                count++;
            } 
            else{
                count = 2;
            }  
            flag = false;
        }
        else{ // If the current number is same as the previous number update count to 1
            count = 1;
        }
        if(maxCount < count){ // If maximum count is less than count, upadte maximum count
            maxCount = count;
        }
    } 
    return maxCount; // Return maximum count
}