#include <iostream>
using namespace std;

int main(){
    int testSize; cin>>testSize;
    while(testSize--){
        int n,m; cin>>n>>m;
        int ans=1, r=1;
        for(int i=m-n+1;i<=m;i++){
            ans=ans*i/r++; 
        } cout<<ans<<endl;
    }
}