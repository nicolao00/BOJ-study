#include <iostream>
using namespace std;

int main(){
    int num;
    int arr[10];
    bool value=false;
    cin>>num;
  
    int size=0;
    while(num!=0){
       arr[size++]=num%10;
       num/=10;
    }
    
    int left, right;
    for(int i=1;i<size;i++){
        left=1; right=1;
        for(int j=0;j<i;j++) left*=arr[j];
        for(int k=size-1;k>=i;k--) right*=arr[k];
        if(right==left) { value=true; break;}
    } 
    if(value) cout<<"YES";
    else cout<<"NO";
}