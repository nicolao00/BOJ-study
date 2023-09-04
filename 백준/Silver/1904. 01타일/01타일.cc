//2236
#include <iostream>
#include <algorithm>
using namespace std;

int dp[1000001];

int main(){
    fill(dp,dp+1000001,-1);
    dp[1]=1; dp[2]=2;
    int inputNum; cin>>inputNum;
    for(int i=3;i<=inputNum;i++)
        dp[i]=(dp[i-1]+dp[i-2])%15746;
    cout<<dp[inputNum];
}