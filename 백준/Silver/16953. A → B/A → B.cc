#include <iostream>
using namespace std;

int main(){
    int a,b; cin>>a>>b; int count=0;
    while(a!=b){
        if(b==0) {cout<<"-1"; return 0;}
        if(b%10==1) b/=10;
        else if(b%2==0) b/=2;
        else {cout<<"-1"; return 0;}
        count++;
    } cout<<count+1;
}