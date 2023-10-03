#include <iostream>
using namespace std;

int dp[1001][10];

int main(){
    for(int i=0;i<10;i++) dp[1][i]=1;
    int len; cin>>len;
    
    for(int i=2;i<=len;i++){
        for(int j=0;j<10;j++){
            for(int k=0;k<=j;k++){
                dp[i][j]+=(dp[i-1][k]%10007);
            }
        }
    }
    int ans=0;
    for(int i=0;i<10;i++)
        ans+=dp[len][i];
    cout<<ans%10007;
}

/*
dp[길이][1의자리수]
자릿수는 음... 1의자리에 새로운 수 더하는 방식으로

dp[2][0]=dp[1][0]
00
dp[2][1]=dp[1][0]+dp[1][1]
01 11
dp[2][2]=dp[1][0]+dp[1][1]+dp[1][2]
02 12 22
.......
dp[2][9]=dp[1][0]+dp[1][1]~~+dp[1][9]
09 19 ~~ 99
dp[3]=dp[2][0~~~9다 더한값]
*/