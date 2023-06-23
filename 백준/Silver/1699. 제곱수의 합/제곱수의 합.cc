#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int dp[100001];

int main(){
    fill(dp,dp+100001,100001);
    int num; cin>>num;
    
    dp[0]=0; dp[1]=1; dp[2]=2; dp[3]=3;
    for(int k=4;k<=num;k++){
        for(int i=sqrt(k); i>0; i--){
            int x2=pow(i,2);
            if(dp[k]>1+dp[k-x2]) dp[k]=1+dp[k-x2];
        }
    } cout<<dp[num];
}