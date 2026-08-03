int removeElement(int* nums, int numsSize, int val) {
    int count = 0;
    for(int i = 0; i < numsSize;){
        if(nums[i] == val){
            int j = i;
            while(j < numsSize - 1){
                nums[j] = nums[j+1];
                j = j + 1;
            }
            numsSize = numsSize - 1;
        }
        else{
            i++;
            count = count + 1;
        }
    }
    return count;
}