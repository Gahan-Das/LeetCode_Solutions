bool isPalindrome(int x) {
    long int copy = x, reverse = 0;
    int r,negative;
    if(x < 0)
    {
        negative = -1;
    }
    else
    {
        negative = 1;
    }
    while(copy != 0)
    {
        r = copy % 10;
        reverse = reverse*10 + r;
        copy /= 10;
    }
    if(x == reverse*negative)
    {
        return true;
    }   
    else
    {
        return false;
    }
        
}