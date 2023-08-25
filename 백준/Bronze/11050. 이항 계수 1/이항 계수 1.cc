#include <iostream>
using namespace std;

template <typename T>
T fact(T num){
    T sum=1;
    for(int i=1;i<=num;i++) sum*=i;
    return sum;
}

int main()
{
    int n; double m;
    cin>>n>>m;
    cout<<fact(n)/(fact(m)*fact(n-(int)m));
}