int minMoves(int* nums, int numsSize) {
    int max = nums[0]; // Initilalize max variable with the first value of the array
    for(int i = 1; i < numsSize; i++){ // To find the maximum value in the array
        max = nums[i] > max ? nums[i] : max;
    }
    int count = 0; // Initlialize count variable to 0
    for(int i = 0; i < numsSize; i++){ // Count the difference between the maximum value and the array value for every array value
        count += max - nums[i];
    }
    return count; // Return the count
} 