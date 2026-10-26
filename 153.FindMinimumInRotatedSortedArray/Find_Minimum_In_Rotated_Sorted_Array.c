int findMin(int* nums, int numsSize) {
    int l = 0;
    int r = numsSize-1;
    int mid = (l+r)/2;
    int min = nums[0];
    while(l < r){
        mid = (l+r) / 2;
        if(nums[mid] < min){
            min = nums[mid];
        }
        if(nums[l] < min){
            min = nums[l];
        }
        if(nums[r] < min){
            min = nums[r];
        }

        if(nums[mid] < nums[l]){
            r = mid-1;
        }
        else{
            l = mid+1;
        }
    }
    return min;
}