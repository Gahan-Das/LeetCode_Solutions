int mySqrt(int x) {
    long int i;
    for(i = 1; i*i <= x; i++ );
    return i-1;
}