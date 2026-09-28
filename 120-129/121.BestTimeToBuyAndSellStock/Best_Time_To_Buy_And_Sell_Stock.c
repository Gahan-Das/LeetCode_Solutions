int maxProfit(int* prices, int pricesSize) {
    int min = prices[0],max = prices[0],maxp = 0;
    for(int i = 0; i < pricesSize; i++)
    {
        if(min > prices[i])
        {
            min = prices[i];
            max = prices[i];
            
        }
        if(max < prices[i])
        {
            max = prices[i];
        }
        if(maxp < (max - min))
        {
            maxp = max - min;
        }
    }
    return maxp;
}