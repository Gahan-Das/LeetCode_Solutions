void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i = 0, j = 0, temp[200], k = 0;
    while(i < m && j < n){
        if(nums1[i] <= nums2[j]){
            temp[k] = nums1[i];
            i++;
        }
        else{
            temp[k] = nums2[j];
            j++;
        }
        k++;
    }
    while(i < m){
        temp[k] = nums1[i];
        i++;
        k++;
    }
    while(j < n){
        temp[k] = nums2[j];
        j++;
        k++;
    }
    for(int i = 0; i < k; i++){
        nums1[i] = temp[i];
    }
}