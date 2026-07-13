#include<stdbool.h>
bool search(int* nums, int numsSize, int target) {
    int l = 0, r = numsSize-1;
    int mid = (l + r) / 2;
    while(l <= r){
        mid = (l + r) / 2;
        if(nums[mid] == target){
            return true;
        }
        else if(nums[l] >= nums[mid]){
            r = mid - 1;
        }
        else{
            l = mid + 1;
        }
    }
    printf("%d", l);
    int left = 0, right = r;
    while(left < right){
        mid = (left + right) / 2;
        if(nums[mid] == target){
            return true;
        }
        else if(nums[mid] < target){
            left = mid+1;
        }
        else{
            right = mid-1;
        }
    }
    left = r, right = numsSize-1;
    while(left < right){
        mid = (left + right) / 2;
        if(nums[mid] == target){
            return true;
        }
        else if(nums[mid] < target){
            left = mid+1;
        }
        else{
            right = mid-1;
        }
    }
    for(int i = 0; i < numsSize; i++){
        if(nums[i] == target){
            return true;
        }
    }
    return false;
}