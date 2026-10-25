int maxProduct(int* nums, int numsSize) {
    if(numsSize == 1){
        return nums[0];
    }
    int maxVal = nums[0];
    int min = 1;
    int max = 1;
    for(int i = 0; i < numsSize; i++){  
        if(min == 0){
            min = nums[i];
            max = nums[i];
            if(maxVal < max){
                maxVal = max;
            }
            continue;
        }
        if(nums[i] < 0){
            int tmp = min;
            min = max * nums[i];
            max = tmp * nums[i];
        }
        else{
            min = min * nums[i];
            max = max * nums[i]; 
        }
        if(maxVal < max){
            maxVal = max;
        }
        if(nums[i] > maxVal){
            maxVal = nums[i];
            max = nums[i];
            continue;
        }
    }
    min = 1;
    max = 1;
    for(int i = numsSize-1; i >= 0; i--){  
        if(min == 0){
            min = nums[i];
            max = nums[i];
            if(maxVal < max){
                maxVal = max;
            }
            continue;
        }
        if(nums[i] < 0){
            int tmp = min;
            min = max * nums[i];
            max = tmp * nums[i];
        }
        else{
            min = min * nums[i];
            max = max * nums[i]; 
        }
        if(maxVal < max){
            maxVal = max;
        }
        if(nums[i] > maxVal){
            maxVal = nums[i];
            max = nums[i];
            min = min * nums[i];
            continue;
        }
    }
    return maxVal;
}