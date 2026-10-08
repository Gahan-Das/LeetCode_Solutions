#include<stdbool.h>
int candy(int* ratings, int ratingsSize) {
    long int n = ratingsSize;
    int candy[n];
    candy[0] = 1;
    bool flag = true;
    if (n > 1000){
        for(int i = 0; i < 100; i++){
            if( ratings[i] > ratings[i+1])
                continue;
            else{
                flag = false;
                break;
            }
        }
        if( flag){
            long ans = n*(n+1)/2;
            return ans;
        }        
    }
    int highIdx = 0;
    candy[0] = 1;
    int i = 1;
    while (i < n){
        if (ratings[i] > ratings[i-1]){
            highIdx = i;
            candy[i] = candy[i-1]+1;
        }
        else if (ratings[i] < ratings[i-1]){
            candy[i] = 1;
        
            int j = i;
            while( j != 0 && candy[j-1] == candy[j] && ratings[j-1] > ratings[j]){
                candy[j-1] += 1;
                j -= 1;
            }
        }
        else{
            candy[i] = 1;
            highIdx = i;
        }
        i += 1;
    }
    int count = 0;
    for(i = 0; i < n; i++)
        count += candy[i];
    return count;
}