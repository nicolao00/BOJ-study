#include <iostream>
#include <algorithm>
using namespace std;
long long dp[101]={0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, };

long long setDp(int i){
    if(dp[i]!=0) return dp[i];
    
    dp[i]=setDp(i-1)+setDp(i-5);
    return dp[i];
}

int main(){
    int testSize; cin>>testSize;
    for(int i=0;i<testSize;i++){
        int temp; cin>>temp;
        setDp(temp);
        cout<<dp[temp]<<"\n";
    }
}