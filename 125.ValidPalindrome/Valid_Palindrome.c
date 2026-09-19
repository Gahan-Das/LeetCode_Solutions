#include<stdbool.h>
bool isPalindrome(char* s) {
    for(int i = 0; s[i] != '\0'; i++){
        if(s[i] >= 65 && s[i] <= 90){
            s[i] = s[i] + 32;
        }
    }
    int i = 0, j = strlen(s);
    while(i < j){
        if(s[i] < 48 || (s[i] > 57 && s[i] < 65) || (s[i] > 90 && s[i] < 97) || s[i] > 122){
            i++;
            continue;
        }
        if(s[j] < 48 || (s[j] > 57 && s[j] < 65) || (s[j] > 90 && s[j] < 97) || s[j] > 122){
            j--;
            continue;
        }
        if(s[i] != s[j]){
            return false;
        }
        i++;
        j--;
    }
    return true;
}