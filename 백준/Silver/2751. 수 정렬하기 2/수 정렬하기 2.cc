#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int> v;
    int size; cin>>size;
    for(int i=0;i<size;i++){int temp; cin>>temp; v.push_back(temp);} sort(v.begin(),v.end());
    for(int i=0;i<size;i++) cout<<v[i]<<"\n";
}