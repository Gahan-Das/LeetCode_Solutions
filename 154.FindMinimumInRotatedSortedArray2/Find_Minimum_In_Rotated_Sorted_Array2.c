int findMin(int* nums, int numsSize) {
    int l = 0, r = numsSize-1, mid, min = nums[0];
    while(l < r)
    {
        mid = (l + r) / 2;
        if(nums[l] < min){
            min = nums[l];
        }
        if(nums[mid] < min){
            min = nums[mid];
        }
        if(nums[r] < min){
            min = nums[r];
        }

        if(nums[mid] < nums[l]){
            r = mid-1;
        }
        else if(nums[mid] > nums[l]){
            l = mid+1;
        }
        else{
            l = l+1;
            r = r-1;
        }
    }
    return min;
}