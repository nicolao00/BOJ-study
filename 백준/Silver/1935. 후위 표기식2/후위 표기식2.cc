#include <iostream>
#include <string>
#include <stack>
#include <vector>
using namespace std;

int main(){
    int numSize; cin>>numSize;
    string cal; cin>>cal;
    stack<double> sta; vector<double> v;
    
    double operand,a,b;
    for(int i=0;i<numSize;i++) {cin>>operand; v.push_back(operand);}
    for(char c:cal){
        if(c>='A'&&c<='Z') sta.push(v[c-'A']);
        else {
            b=sta.top(); sta.pop(); a=sta.top(); sta.pop();
            if(c=='+') sta.push(a+b);
            if(c=='-') sta.push(a-b);
            if(c=='*') sta.push(a*b);
            if(c=='/') sta.push(a/b);
        }
    } cout<<fixed; cout.precision(2); cout<<sta.top();
}