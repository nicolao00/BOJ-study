#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<string> hear, see, both;
    int n,m, ans=0; cin>>n>>m;
    string temp;
    
    for(int i=0;i<n;i++){
        cin>>temp;
        hear.push_back(temp);
    }
    for(int i=0;i<m;i++){
        cin>>temp;
        see.push_back(temp);
    }
    sort(see.begin(),see.end());
    sort(hear.begin(),hear.end());
    
    int h=0, s=0;
    while(h<hear.size() && s<see.size()){
        if(hear[h]==see[s]){
            ans++; both.push_back(hear[h]);
        }
        if(hear[h]>see[s])
            s++;
        else
            h++;
    }
    
    cout<<ans<<'\n';
    sort(both.begin(),both.end());
    for(int i=0;i<both.size();i++)
        cout<<both[i]<<'\n';
}