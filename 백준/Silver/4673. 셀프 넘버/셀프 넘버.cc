#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int d(int num){
    int sum=num;
    while(num!=0){
        sum=sum+num%10;
        num/=10;
    } return sum;
}

int main(){
    vector<int> v;
    for(int i=0;i<9974;i++) v.push_back(d(i));
    sort(v.begin(), v.end());
    
    int size=v.size();
    for(int i=0;i<size;i++){
        for(int k=v[i]+1;k<v[i+1];k++) cout<<k<<endl;
    }
}