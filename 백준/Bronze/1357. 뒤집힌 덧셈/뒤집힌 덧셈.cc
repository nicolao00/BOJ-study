#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int Rev(int num){
    int sum=0;
    string a;
    a=to_string(num);
    
    for(int i=a.size()-1;i>=0;i--){
        sum=sum+(a[i]-'0')*pow(10,i);
    }return sum;
}

int main()
{
    int x,y;
    cin>>x>>y;
    cout<<Rev(Rev(x)+Rev(y));
}