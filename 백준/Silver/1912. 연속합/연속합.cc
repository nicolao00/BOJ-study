#include <iostream>
using namespace std;

int dp[100001];

int main(){
    int size, sum; cin>>size;

    for(int i=0;i<size;i++){
        int num; cin>>num;
        dp[i]=num;
        if(i==0) {sum=num; continue;}
        if(dp[i]<dp[i-1]+num) dp[i]=dp[i-1]+num;
        if(dp[i]>sum) sum=dp[i];
    }cout<<sum;
}