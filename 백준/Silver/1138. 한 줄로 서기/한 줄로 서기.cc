#include <iostream>
using namespace std;

int main(){
    int size; cin>>size;
    int arr[size]={0,};
    
    for(int i=1;i<=size;i++){
        int tall; cin>>tall;
        
        for(int k=0;k<size;k++){
            if(arr[k]==0&&tall==0){ arr[k]=i; break;}
            else if(arr[k]==0) tall--;
        }
    }
    for(int i=0;i<size;i++) cout<<arr[i]<<" ";
}