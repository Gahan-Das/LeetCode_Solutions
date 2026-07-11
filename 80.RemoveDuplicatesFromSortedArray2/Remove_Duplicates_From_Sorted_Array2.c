int removeDuplicates(int* nums, int numsSize) {
    int count = 1, curr = nums[0], ansSize = 1, max = nums[numsSize-1], flag = 1;
    if(numsSize == 1){
        return 1;
    }
    for(int i = 0; i < numsSize; i++){
        if(nums[i] == curr){
            continue;
        }
        flag = 0;
        break;
    }
    if(flag){
        return 2;
    }
    if(nums[numsSize-1] == nums[numsSize-2]){
        flag = 1;
    }
    int flag2 = 0;
    for(int i = 1; i < numsSize; i++){
        if(nums[i] == curr){
            count++;
            ansSize++;
        }
        else{
            count = 1;
            curr = nums[i];
            ansSize++;
        }
        if(count > 2){
            flag2 = 1;
            ansSize--;
            int j = i;
            int val = nums[i];
            while(j < numsSize-1){
                nums[j] = nums[j+1];
                j++;
            }
            i--;
            if(nums[i] == max && count >= 2){
                break;
            }    
        }
    }
    if(flag==1){
        return ansSize;
    }
    else{
        if(flag2){
            return ansSize-1;
        }
        else{
            return ansSize;
        }
    }
    
}