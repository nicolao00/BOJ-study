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