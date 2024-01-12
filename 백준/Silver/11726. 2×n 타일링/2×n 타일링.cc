#include <iostream>
#include <algorithm>
using namespace std; 
int dp[1001];

int solved(int num){
    if(num==1||num==2||dp[num]!=-1) return dp[num];
    if(dp[num]==-1){
        dp[num]=(solved(num-1)+solved(num-2))%10007;
    } return dp[num];
}

int main(){ 
    fill(dp,dp+1001,-1);
    dp[1]=1; dp[2]=2;
    int length; cin>>length; 
    cout<<solved(length);
}