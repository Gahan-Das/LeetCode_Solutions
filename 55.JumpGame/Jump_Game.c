#include<stdbool.h>
bool canJump(int* nums, int numsSize) {
    if(numsSize == 1){
        return true;
    }
    int jump[1000000] = {0};
    if (nums[0] > 0){
        jump[0] = 1;
    }
    for(int i = 0; i < numsSize; i++){
        int limit = numsSize < i+nums[i] ? numsSize : i+nums[i] ;
        for(int j = i+1; j <= limit; j++){
            if (jump[i] == 1){
                jump[j] = 1;
            }
        }
    }
    if(jump[numsSize-1] == 1){
        return true;
    }
    
    return false;
}