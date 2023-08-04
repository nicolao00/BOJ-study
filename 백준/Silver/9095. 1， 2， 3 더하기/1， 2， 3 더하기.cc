//2208

#include <iostream>
using namespace std;

int fact[11]={0,1,2,6,24,120,720,5040,40320,362880,3628800};

int f(int three, int two, int one){
    int count=fact[three+two+one];
    if(three!=0) count/=fact[three];
    if(two!=0) count/=fact[two];
    if(one!=0) count/=fact[one];
    return count;
}

int main(){ 
    int testSize; cin>>testSize; 
    for(int i=0;i<testSize;i++){
        int num; cin>>num; int sum=0;
        for(int k=num/3; k>=0; k--){
            for(int t=(num-3*k)/2; t>=0; t--){
                sum+=f(k,t,(num-3*k-2*t));
            }        
        }cout<<sum<<"\n";
    }
}