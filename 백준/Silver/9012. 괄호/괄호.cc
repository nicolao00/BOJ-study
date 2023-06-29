#include <iostream>
#include <string>
#include <stack>
using namespace std;
//2156
int main(){
    stack<char> st;
    int size; string str;
    cin>>size;

    for(int i=0;i<size;i++){
        cin>>str; int length=str.length(); 
        for(int k=0;k<length;k++){
            if(str[k]=='(') st.push(str[k]);
            if(str[k]==')'){ 
                if(st.empty()) {st.push(')'); break;}
                st.pop();
            }
        }if(st.empty()) cout<<"YES"<<endl; 
        else {cout<<"NO"<<endl; while(!st.empty()) st.pop();}
    }
}