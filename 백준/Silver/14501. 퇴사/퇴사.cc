#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;

int dp[17];

int main(){
    int day; cin>>day;
    vector<pair<int,int>> v;
     
    v.push_back(make_pair(0,0)); // v[0]을 채우기 위한 쓰레기값
    for(int i=0;i<day;i++){
        int takeD, price; cin>>takeD>>price;
        v.push_back(make_pair(takeD, price));
    }
    
    // dp[x]란 x일~max일동안 가능한 경우의수들 중 가장 큰 보상값 (무조건 v[x].second를 포함해야되네??)
    fill(dp,dp+17,0);
    
    for(int i=day;i>0;i--){
        for(int k=i+v[i].first;k<=day+1;k++){
            if(dp[i]<v[i].second+dp[k]){
                dp[i]=v[i].second+dp[k];
            }            
        }
    }
    int max=0;
    for(int i=1;i<=day;i++){
        if(max<dp[i]) max=dp[i];
    } cout<<max;
}