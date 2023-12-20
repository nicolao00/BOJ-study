#include <iostream>
#include <queue>
using namespace std;

int main(){
    int size, set;
    queue<int> q, answer;
    cin>>size>>set;
    
    for(int i=1;i<=size;i++) q.push(i);
    
    int idx=1;
    while(q.size()!=0){
        if(idx%set==0){answer.push(q.front()); q.pop();}
        else {q.push(q.front()); q.pop();} idx++;
    } cout<<"<"; 
    while(answer.size()!=1){cout<<answer.front()<<", "; answer.pop();}
    cout<<answer.front()<<">";
}