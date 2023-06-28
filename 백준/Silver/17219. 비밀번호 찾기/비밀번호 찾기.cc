#include <map>
#include <iostream>
using namespace std;

int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n,m; cin>>n>>m;
    string site, password; 
    map<string, string> memo;

    for(int i=0;i<n;i++){
        cin>>site>>password;
        memo[site]=password;
    }
    for(int i=0;i<m;i++){
        cin>>site;
        cout<<memo[site]<<'\n';
    }
}