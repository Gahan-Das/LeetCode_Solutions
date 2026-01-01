int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    
    for(int i = 0; i < numsSize; i++)
    {
        for(int j = 0; j < numsSize; j++)
        {
            if((i != j )&&( nums[i]+nums[j] == target))
            {
                int* result = (int*)malloc(2*sizeof(int));
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    return 0;
}