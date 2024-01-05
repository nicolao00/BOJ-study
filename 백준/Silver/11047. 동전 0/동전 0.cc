#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> v;
    int lSize, price, temp; cin>>lSize>>price;
    for(int i=0;i<lSize;i++){
        cin>>temp; v.push_back(temp);
    }
    int idx=v.size(); int total=0, coinSize=0;
    while(idx--&&price){
        int temp=price/v[idx];
        price-=v[idx]*temp; coinSize+=temp;
    } cout<<coinSize;
}