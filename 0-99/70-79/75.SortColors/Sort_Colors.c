
void sortColors(int* nums, int numsSize) {
    int i = 0, right = numsSize-1, prev = numsSize-1;
    if(numsSize == 2){
        if(nums[0] > nums[1]){
            int temp = nums[0];
            nums[0] = nums[1];
            nums[1] = temp;
        }
    }
    while(i <= prev){
        if(nums[i] == 0){
            i++;
        }
        else if(nums[i] == 2){
            int tmp = nums[i];
            nums[i] = nums[right];
            nums[right] = tmp;
            if(right == prev)
                prev--;
            right--;
        }
        else{
            int tmp = nums[i];
            nums[i] = nums[prev];
            nums[prev] = tmp;
            prev--;
        }
    }
}