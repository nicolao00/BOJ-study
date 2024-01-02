//2147
#include <iostream>
#include <stdio.h>
#include <deque>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int turnCount, matrix[4][8]; //[몇번째 톱니바퀴][몇번째 상태]
int visited[4], score[4]={1,2,4,8}; // 이미 돌렸던 gear
deque<int> deq[4]; 
queue<pair<int,int>> que;

void bfs(){
    while(!que.empty()){
        int gear=que.front().first, direction=que.front().second; que.pop();
        int first=deq[gear][0]; int end=deq[gear][7]; 
        if(direction==-1){ // 아 알겠다 deqeu<int> deq여서 deq.pop_front()해도 안없어지나?
            deq[gear].pop_front(); deq[gear].push_back(first);
        }
        if(direction==1){
            deq[gear].pop_back(); deq[gear].push_front(end);
        }
    }
}


void dfs(int gear, int direction){
    visited[gear]=1; que.push(make_pair(gear,direction));
    
    if(gear-1>=0 && !visited[gear-1]){
        if(deq[gear][6]!=deq[gear-1][2]) dfs(gear-1,direction*-1);
        else visited[gear-1]=1;
    }
    if(gear+1<4 && !visited[gear+1]){
        if(deq[gear][2]!=deq[gear+1][6]) dfs(gear+1,direction*-1);
        else visited[gear+1]=1;
    }
    
}

int main(){
    for(int gear=0;gear<4;gear++){
        for(int toothIdx=0;toothIdx<8;toothIdx++){
            scanf("%1d", &matrix[gear][toothIdx]);
            deq[gear].push_back(matrix[gear][toothIdx]);
        }
    }
    cin>>turnCount;
    for(int i=0;i<turnCount;i++){
        int gearNum,direction; cin>>gearNum>>direction;
        dfs(gearNum-1,direction); bfs(); fill(visited,visited+4,0);
    }
    int ans=0;
    for(int i=0;i<4;i++){
        if(deq[i][0]) ans+=score[i];
    } cout<<ans;
}