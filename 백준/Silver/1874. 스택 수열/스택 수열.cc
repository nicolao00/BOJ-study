#include <iostream>
#include <stack>
#include <queue>
using namespace std;

int main(){
    int size; cin>>size;
    stack<int> s;
    queue<char> ans;
    int value=1;
    
    int max=0; int top;
    while(size--){
        cin>>top;
        
        if(top>max){        
            for(;max<top;max++){s.push(max+1); ans.push('+');}
        }
        else if(top<max) {
            if(s.top()!=top) {value=0; break;}
        }
        else {
            if(s.empty()) {value=0; break;}
        }s.pop(); ans.push('-');
    }
    
    if(value){
        while(!ans.empty()){
            cout<<ans.front()<<"\n"; ans.pop();
        }
    } else cout<<"NO";
}