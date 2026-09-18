int maxProfit(int* prices, int pricesSize) {
    int min = prices[0], max = prices[0], profit = 0, tprofit = 0;
    for(int i = 0; i < pricesSize; i++)
    {
        if(prices[i] < max || prices[i] < min)
        {
            tprofit += profit;
            profit = 0;
            min = prices[i];
            max = prices[i];
        }
        if(min > prices[i])
        {
            min = prices[i];
            max = prices[i];
        }
        if(max < prices[i])
        {
            max = prices[i];
        }
        if(profit < max-min)
        {
            profit = max - min;
        }
    }
    if(prices[pricesSize - 1] == max)
    {
        tprofit += profit;
    }
    return tprofit;
}