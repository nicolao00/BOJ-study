//2237
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    string temp; 
    stack<int> st;
    bool val=true;
    int length=0;
    while(1){
        val=true; getline(cin,temp,'.'); cin.ignore();
        if(temp.empty()) break;
        length=temp.length();
        for(int i=0;i<length;i++){
            if(temp[i]=='(') st.push(1);
            if(temp[i]==')'){
                if(st.size()==0||st.top()!=1){val=false; break;}
                else st.pop();
            }
            if(temp[i]=='[') st.push(2);
            if(temp[i]==']'){
                if(st.size()==0||st.top()!=2){val=false; break;}
                else st.pop();
            }
        }if(val&&st.size()==0) cout<<"yes"<<endl; else cout<<"no"<<endl;
        while(!st.empty()) st.pop();
    }
}