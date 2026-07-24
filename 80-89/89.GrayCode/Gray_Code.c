/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int binInt(long int n){
    int num = 0, count = 0;
    while(n > 0){
        num = (int)pow(2,count++)*(n%10) + num;
        n /= 10;
    }
    // printf("\t%d", num);
    return num;
}
int binGray(long int n){
    long int num = 0, copy = n;
    int count = 0;
    while(copy > 0){
        num = ((copy%100)/10 ^ copy%10)*(int)pow(10,count++) + num;
        copy /= 10;
    }
    // printf("\t%ld", num);
    return binInt(num);
}
int intBin(int n){
    long int num = 0;
    int x = n, count = 0;
    while(x > 0){
        num = (x % 2)*(int)pow(10,count++) + num;
        x = x/2;
    }
    // printf("\n%ld",num);
    return binGray(num);
}
int* grayCode(int n, int* returnSize) {
    int* answer = (int*)malloc((int)pow(2,n)*sizeof(int));
    int ans[70000] = {0};
    for(int i = 0; i < (int)pow(2,n); i++){
        answer[i] = intBin(i);
    } 
    // for(int i = 0; i < (int)pow(2,n); i++)
    //     printf("%d\t", *(answer+i));
    *returnSize = (int)pow(2,n);
    return answer;
}
int main(){
    int n = 10;
    int size;
    int* arr = grayCode(n, &size);
    for(int i = 0; i < size; i++){
        printf("%d\t", arr[i]);
    }
}