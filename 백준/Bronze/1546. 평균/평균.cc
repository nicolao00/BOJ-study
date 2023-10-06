#include <iostream>

using namespace std;
//22:14
int main()
{
    int count=0;
    double sum=0;
    double rest=0;
    double arr[1000];
    
    cin>>count;
    for(int i=0;i<count;i++) {
        cin>>arr[i]; 
        sum+=arr[i];
    }
    
    double max;
    max=arr[0];
    for(int i=0;i<count;i++){
        if(max<arr[i]) max=arr[i];
    }

    rest=sum/max*100/count;
    cout<<rest;
}