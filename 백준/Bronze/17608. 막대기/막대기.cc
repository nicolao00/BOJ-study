#include <iostream>
#include <stack>

using namespace std;

int main(){
    int size, height; cin>>size;
    stack<int> sta;
    for(int i=0;i<size;i++){
        cin>>height; sta.push(height);
    } int max=sta.top(); sta.pop(); int count=1;
    while(sta.size()!=0){
        if(sta.top()>max){max=sta.top(); sta.pop(); count++;}
        else sta.pop();
    }cout<<count;
}