/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int binInt(long int n){
    int num = 0, count = 0;
    while(n > 0){
        num = (long int)pow(2,count++)*(n%10) + num;
        n /= 10;
    }
    return num;
}
int binGray(long int n){
    long int num = 0, copy = n;
    int count = 0;
    while(copy > 0){
        num = ((copy%100)/10 ^ copy%10)*(long int)pow(10,count++) + num;
        copy /= 10;
    }
    return binInt(num);
}
int intBin(int n){
    long int num = 0;
    int x = n, count = 0;
    while(x > 0){
        num = (x % 2)*(long int)pow(10,count++) + num;
        x = x/2;
    }
    return binGray(num);
}
int* grayCode(int n, int* returnSize) {
    int* answer = (int*)malloc((long int)pow(2,n)*sizeof(int));
    for(int i = 0; i < (long int)pow(2,n); i++){
        answer[i] = intBin(i);
    } 
    *returnSize = (int)pow(2,n);
    return answer;
}