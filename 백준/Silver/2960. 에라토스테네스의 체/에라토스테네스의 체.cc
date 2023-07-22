//2255
#include <iostream>
#include <vector>
using namespace std;

int main(){
    int num,idx; cin>>num>>idx;
    vector<int> v; vector<int>::iterator it;
    for(int i=2;i<=num;i++) v.push_back(i);
    
    int count=0;
    while(!v.empty()){
        int temp=v[0];
        for(it=v.begin();it!=v.end();){
            if(*it%temp==0){
                ++count; 
                if(count==idx){cout<<*it; return 0;}
                it=v.erase(it);
            }
            else ++it;
        }
    }
}