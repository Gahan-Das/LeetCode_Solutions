int reverse(int x){
    long int copy = x;
    long int reverse = 0;
    int r;
    while(copy != 0)
    {
        r = copy % 10;
        copy /= 10;
        reverse = reverse*10 + r;
    }
    if (reverse < -(long int)pow(2,31) || reverse > (long int)pow(2,31))
    {
        return 0;
    }
    return reverse;
}