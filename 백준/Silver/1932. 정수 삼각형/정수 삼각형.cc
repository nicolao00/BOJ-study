#include <iostream>
#include <algorithm>
using namespace std;

int dp[501][501];

int main(){
    int topH,temp,ans; cin>>topH;
    fill(dp[0],dp[500],-1);
    cin>>temp; dp[1][0]=temp; ans=temp;
    for(int h=2;h<=topH;h++){
        for(int i=0;i<h;i++){
            cin>>temp;
            dp[h][i]=temp+max(dp[h-1][i-1],dp[h-1][i]);
            if(ans<dp[h][i]&&h==topH) ans=dp[h][i];
        }
    } cout<<ans;    
}