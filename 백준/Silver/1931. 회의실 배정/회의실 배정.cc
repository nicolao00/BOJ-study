#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int main(){
    vector<pair<int,int>> v;
    int conferSize; cin>>conferSize;
    for(int i=0;i<conferSize;i++){
        int sTime, eTime; cin>>sTime>>eTime; 
        v.push_back(make_pair(eTime,sTime)); // 종료, 시작시간 순서로 짝 생성
    } sort(v.begin(),v.end());
    
    int sTime=v[0].second, eTime=v[0].first, count=1; 
    for(int i=1;i<conferSize;){
        if(eTime<=v[i].second){
            count++; sTime=v[i].second; eTime=v[i].first;
        } i++;
    } cout<<count;
}