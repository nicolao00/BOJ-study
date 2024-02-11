#include <iostream>
#include <deque>
#include <queue>
using namespace std;

int main(){
    int size, outSize;    // N,M
    deque<int> dq;
    queue<int> q;    //  출력할 원소 위치 저장할 큐
    cin>>size>>outSize;
    
    int temp;
    for(int i=0;i<outSize;i++){ cin>>temp; q.push(temp); }
    for(int i=1;i<=size;i++) dq.push_back(i);
    
    int count=0, idx, work=0; // 찾은 원소 개수, 찾는 원소의 위치[배열의 인덱스], 연산량
    while(count!=outSize){
        for(int i=0;i<dq.size();i++){
            if(q.front()==dq[i]){idx=i; break;}
        }
        if(dq.front()!=q.front()){
            if(idx<dq.size()-idx) {
                for(int k=0;k<idx;k++) {dq.push_back(dq.front()); dq.pop_front();  work++;}
            }
            else{ 
                for(int k=0;k<dq.size()-idx;k++) {dq.push_front(dq.back()); dq.pop_back(); work++;}
            }    
        } dq.pop_front(); count++; q.pop(); // 맨앞으로 온 찾은 원소 삭제  
    } cout<<work;
}