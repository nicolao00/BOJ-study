#include <iostream>

using namespace std;
int price[1001];
int dp[1001];

int main(){
    int N; cin>>N;
    for(int i=1;i<=N;i++)
        cin>>price[i];
    
    dp[1]=price[1];    
    for(int i=2;i<=N;i++){
        int total=0;
        for(int k=0;k<=i;k++){
            total=price[k]+dp[i-k];
            if(dp[i]<total) dp[i]=total;
        }
    } cout<<dp[N];
}