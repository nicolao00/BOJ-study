//2143
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dp[1001];

int main(){
    vector<int> v;
    int personSize; cin>>personSize;
    for(int i=0;i<personSize;i++){
        int temp; cin>>temp; v.push_back(temp);
    } sort(v.begin(),v.end());
    
    dp[0]=v[0]; int sum=dp[0];
    for(int i=1;i<personSize;i++){
        dp[i]=dp[i-1]+v[i]; sum+=dp[i];
    } cout<<sum;
}