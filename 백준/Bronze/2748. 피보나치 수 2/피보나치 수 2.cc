#include <iostream>
using namespace std;

long long fib(long long a, long long b){
    return a+b;
}

int main()
{
    long long first=0, second=1, temp;
    int count=2, input;
    cin>>input;
    switch(input){
        case 0:
        cout<<first;
        break;
        
        case 1:
        cout<<second;
        break;
        
        default:
        for(;count<=input;count++){
        temp=second;
        second=fib(first, second);
        first=temp;
        }cout<<second; break;
    }
}