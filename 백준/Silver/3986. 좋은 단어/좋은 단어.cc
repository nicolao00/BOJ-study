#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(){
    stack<char> sta; 
    string str; 
    int testSize, ans=0; 
    
    cin>>testSize;
    for(int k=0;k<testSize;k++){
        cin>>str; 
        for(int i=0;i<str.length();i++){
            if(sta.empty()) sta.push(str[i]);
            else if(sta.top()==str[i]) sta.pop();
            else sta.push(str[i]);
        } 
        if(sta.empty()) ans++;
        else {while(!sta.empty()) sta.pop();}
    }cout<<ans;
}