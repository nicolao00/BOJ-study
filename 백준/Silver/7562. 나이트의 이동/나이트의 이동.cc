#define MAX 301
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int dX[8]={1,2,2,1,-1,-2,-2,-1}, dY[8]={2,1,-1,-2,-2,-1,1,2};
int ansX,ansY,wid;
bool matrix[MAX][MAX];

void bfs(int x,int y){
    queue<pair<int,int>> que;
    que.push(make_pair(x,y)); matrix[y][x]=true;
    int count=0, eX=que.front().first, eY=que.front().second; 
    
    while(1){
        int idx=que.size();
        while(idx--){
            eX=que.front().first, eY=que.front().second; 
            que.pop();
            if(eX==ansX && eY==ansY) {cout<<count<<endl; return;}
            for(int i=0;i<8;i++){
                int nX=eX+dX[i], nY=eY+dY[i];
                if(nX>=0 && nX<wid && nY>=0 && nY<wid && !matrix[nY][nX]){
                    que.push(make_pair(nX,nY)); matrix[nY][nX]=true;
                }
            } 
        }count++;
    }
}

int main(){
    int testSize; cin>>testSize;
    while(testSize--){
        cin>>wid;
        int x,x1,y,y1; cin>>x>>y; cin>>x1>>y1;
        ansX=x1; ansY=y1; bfs(x,y); 
        fill(matrix[0],matrix[MAX],0);
    }
}