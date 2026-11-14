int minimumSumSubarray(int* nums, int numsSize, int l, int r) {
    int val;
    int minVal = 10000000;
    
    for(int i = l; i <= r; i++){
        int j = 0;
        int k = j+i-1;
        val = 0;
        for(int l = j; l <= k; l++){
            val += nums[l];
        }
        if(minVal > val && val > 0){
            minVal = val;
        }
        while(k < numsSize-1){
            val -= nums[j];
            j++;
            k++;
            val += nums[k];
            if(minVal > val && val > 0){
                minVal = val;
            }
        }
    }
    if(minVal == 10000000){
        return -1;
    }
    else{
        return minVal;
    }
}