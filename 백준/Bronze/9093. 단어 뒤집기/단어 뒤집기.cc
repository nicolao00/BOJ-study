#include <iostream>
#include <stack>
#include <vector>

using namespace std;
int main(){
    stack<char> sta;
    int testSize; cin>>testSize; cin.ignore();
    for(int i=0;i<testSize;i++){
        string alp; getline(cin,alp,'\n');
        for(int k=0;k<alp.length();k++){
            if(alp[k]==' '){
                while(!sta.empty()){cout<<sta.top(); sta.pop();} 
                cout<<' ';
            }
            else sta.push(alp[k]);
        } while(!sta.empty()){cout<<sta.top(); sta.pop();} cout<<endl;
    }
}