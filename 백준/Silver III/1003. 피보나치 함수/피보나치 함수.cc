#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int dp[41][1]={0,};

int main(){
    dp[0][0]=1; dp[0][1]=0; dp[1][0]=0; dp[1][1]=1;
    int testSize; cin>>testSize;
    vector<int> v; 
    
    int max=0;
    for(int i=0;i<testSize;i++){
        int temp; cin>>temp; v.push_back(temp);
        if(max<temp) max=temp;
    }

    for(int i=2;i<=max;i++){
        dp[i][0]=dp[i-1][0]+dp[i-2][0];
        dp[i][1]=dp[i-1][1]+dp[i-2][1];
    }
    for(int i=0;i<testSize;i++) {cout<<dp[v[i]][0]<<" "<<dp[v[i]][1]<<"\n";}
}