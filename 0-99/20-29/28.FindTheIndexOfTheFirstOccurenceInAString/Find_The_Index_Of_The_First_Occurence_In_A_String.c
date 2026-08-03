int strStr(char* haystack, char* needle) {
    for(int i = 0; haystack[i] != '\0'; i++){
        if(haystack[i] != needle[0]){
            continue;
        }
        int flag = 1;
        for(int j = 1; needle[j] != '\0'; j++){
            if(haystack[j+i] != needle[j]){
                flag = 0;
                break;
            }
        }
        if(flag){
            return i;
        }
    }
    return -1;
}