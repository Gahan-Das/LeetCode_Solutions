int removeDuplicates(int* nums, int numsSize) {
    int count = 1;
    for(int i = 1; i < numsSize; ){
        if(nums[i] == nums[i-1]){
            int j = i;
            while(j < numsSize-1){
               *(nums+j) = *(nums+j+1);
                j = j + 1;
            }
            numsSize = numsSize - 1;
        }else{
            count = count + 1;
            i++;
            
        }
    }
    return count;
}