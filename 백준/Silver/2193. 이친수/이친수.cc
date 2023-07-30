#include<iostream>
using namespace std;
int main(){
    int i,n; cin>>n;
    long long int d[91];
    d[0]=0; d[1]=1;
    for(i=2;i<=n;i++){
        d[i] = d[i-1]+d[i-2];
    }
    printf("%lld", d[n]);
}