#include <utility>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<pair<int,int>> v;
    int pointSize; cin>>pointSize;
    for(int i=0;i<pointSize;i++){
        int x,y; cin>>x>>y;
        v.push_back(make_pair(x,y)); 
    } sort(v.begin(),v.end()); 
    for(int i=0;i<pointSize;i++) cout<<v[i].first<<" "<<v[i].second<<"\n";
}