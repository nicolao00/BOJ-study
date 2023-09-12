//2155
#include <iostream>
#include <utility>
#include <queue>
using namespace std;
int wid,apple,ans;
queue<pair<int,char>> que;
int matrix[101][101], occupy[101][101];
int dx[4]={0,1,0,-1}, dy[4]={1,0,-1,0};

void bfs(){
    int idx=1, x=0,y=0, end; occupy[0][0]=1; ans=1; char distance='D';
    queue<pair<int,int>> tail; tail.push(make_pair(0,0));
    while(1){
        if(que.empty()) end=9999999;
        else { end=que.front().first; distance=que.front().second; que.pop();} 
        
        for(;ans<=end;ans++){
            x+=dx[idx], y+=dy[idx];
            if(y<0 || y>=wid || x<0 || x>=wid || occupy[y][x]){cout<<ans; return;}
            if(matrix[y][x]!=1) { 
                occupy[tail.front().first][tail.front().second]=0; tail.pop(); 
            } tail.push(make_pair(y,x));
            matrix[y][x]=0;occupy[y][x]=1;
        } if(distance=='L') idx=(idx+1)%4; if(distance=='D') idx=(idx+3)%4;
    }
}

int main(){
    cin>>wid>>apple; 
    for(int i=0;i<apple;i++){
        int x,y; cin>>y>>x; matrix[y-1][x-1]=1;
    }
    int change; cin>>change; 
    for(int i=0;i<change;i++){
        int temp; char tem; 
        cin>>temp>>tem; que.push(make_pair(temp,tem));
    } bfs();
}