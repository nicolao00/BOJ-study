#define MAX 51
#include <iostream>
#include <queue>
using namespace std;

int matrix[MAX][MAX], visited[MAX][MAX];
int cX[4]={0,1,0,-1}, cY[4]={1,0,-1,0};

void bfs(int y, int x){
    queue<pair<int,int>> que;
    que.push(make_pair(y,x));
    
    while(!que.empty()){
        int eY=que.front().first, eX=que.front().second; que.pop();
        for(int i=0;i<4;i++){
            int nY=eY+cY[i], nX=eX+cX[i];
            if(matrix[nY][nX]&&!visited[nY][nX]){
                visited[nY][nX]=1; que.push(make_pair(nY,nX));
            }
        }
    }
}

int main(){
    int testSize; cin>>testSize;
    for(int i=0;i<testSize;i++){
        int x,y,carrotSize,count=0; cin>>x>>y>>carrotSize;
        for(int k=0;k<carrotSize;k++){
            int dx,dy; cin>>dx>>dy; matrix[dy][dx]=1;
        }
        for(int j=0;j<y;j++){
            for(int t=0;t<x;t++){
                if(matrix[j][t]&&!visited[j][t]){
                    visited[j][t]=1; count++; bfs(j,t);
                }
            }
        } cout<<count<<endl;
        for(int i=0;i<MAX;i++){
            fill(matrix[i],&matrix[i][MAX],0); fill(visited[i],&visited[i][MAX],0);
        }
    }
}