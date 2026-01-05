int myAtoi(char* s) {
    int i = 0,negative = 0,len = strlen(s);
    __int128 num = 0;
    while(s[i] == ' ' && i != len)
    {
        i++;
    }
    if(s[i] == '-')
    {
        negative = 1;
        i++;
    }
    else if(s[i] == '+')
    {
        i++;
    }
    while(s[i] >= 48 && s[i] <= 57 && i != len)
    {
        num = num*10 + (s[i] - '0');
        i++;
        if(num <= -(long int)pow(2,31) || num >= (long int)pow(2,31))
        {
            if(negative)
                return (long int)pow(2,31);
                
            else
                
                return (-1)*(long int)pow(2,31)-1;
        } 
    }
    if(negative)
    {
        return num*(-1);
    }
    else
    {
        return num;
    }

    

}