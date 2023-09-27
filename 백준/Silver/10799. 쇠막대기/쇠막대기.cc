//2234
#include <iostream>
#include <stack>
using namespace std;

int main(){
    string str; cin>>str;
    stack<char> sta;
    
    int stickSum=0; sta.push('('); 
    for(int i=1;i<str.length();i++){
        if(str[i]=='(') sta.push('(');
        if(str[i]==')'){
            sta.pop(); 
            if(str[i-1]!=')') stickSum+=sta.size();
            else stickSum++;
        } 
    }cout<<stickSum;
}