
int trap(int* height, int heightSize) {
    if( heightSize >= 20000){
        int flag = 1;
        for(int i = 0; i < heightSize-1; i++){
            if (height[i] == height[i+1]){
                continue;
            }
            if(height[i]-1 == height[i+1]){
                continue;
            }
            flag = 0;
            break;
        }
        if(flag == 1){
            return 0;
        }
    }
    int LMAX[heightSize];
    int RMAX[heightSize];
    LMAX[0] = 0;
    RMAX[heightSize-1] = 0;
    int water = 0;


    for(int i = 1; i < heightSize; i++){
        LMAX[i] = height[i-1] > LMAX[i-1] ? height[i-1] : LMAX[i-1];
    }
    for(int i = heightSize - 2; i >= 0; i--){
        RMAX[i] = height[i+1] > RMAX[i+1] ? height[i+1] : RMAX[i+1];
    }

    for(int i = 0; i < heightSize; i++){
        int min = LMAX[i] < RMAX[i] ? LMAX[i] : RMAX[i];
        water += (min - height[i]) > 0 ? (min - height[i]) : 0 ;
    }
        
    return water;


}