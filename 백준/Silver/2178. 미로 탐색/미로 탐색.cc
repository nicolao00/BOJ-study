#define MAX 101
#include <iostream>
#include <queue>
#include <utility>
#include <algorithm>
#include <tuple>
using namespace std;

int matrix[MAX][MAX], visited[MAX][MAX];
int dy[4]={1,0,-1,0}, dx[4]={0,1,0,-1};
vector<int> v;
int N,M;

void bfs(int y,int x){
    visited[y][x]=1;
    queue<tuple<int,int,int>> que;
    que.push(make_tuple(y,x,1));
    
    while(!que.empty()){
        int a=get<0>(que.front()), b=get<1>(que.front()), c=get<2>(que.front());
        if(a==N&&b==M){v.push_back(c); return;}
        que.pop();
        
        for(int i=0;i<4;i++){
            int nY=a+dy[i],nX=b+dx[i];
            if(matrix[nY][nX]&&!visited[nY][nX]){
                visited[nY][nX]=1; que.push(make_tuple(nY,nX,c+1));
            }
        }
    }
}

int main(){
    cin>>N>>M;
    for(int i=1;i<=N;i++){
        for(int j=1;j<=M;j++){
            scanf("%1d", &matrix[i][j]);
        }
    }
    bfs(1,1); cout<<v[0];
}