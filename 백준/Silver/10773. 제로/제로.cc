//2336
#include <iostream>
#include <stack>
using namespace std;

int main(){
    stack<int> stc;
    int line, num, sum=0;
    cin>>line;
    for(int i=0;i<line;i++){
        cin>>num;
        if(num==0) stc.pop();
        else stc.push(num);
    }
    while(!stc.empty()){
        sum+=stc.top(); stc.pop();
    } cout<<sum;
    return 0;
}