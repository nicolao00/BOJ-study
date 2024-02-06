#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 101
using namespace std;

int matrix[MAX][MAX], visited[MAX][MAX];
int changeX[4]={0,1,0,-1},changeY[4]={1,0,-1,0};
int m,n,k;
vector<int> v;

void dfs(int x, int y, int idx){
    visited[y][x]=1; v[idx]++;
    
    for(int i=0;i<4;i++){
        int nY=y+changeY[i], nX=x+changeX[i];
        if(nY>=0 && nY<n && nX>=0 && nX<m && !matrix[nY][nX] && !visited[nY][nX]) 
            dfs(nX,nY,idx);
    }
}

int main(){
    cin>>n>>m>>k;
    for(int i=0;i<k;i++){
        int y,x,y2,x2; cin>>x>>y>>x2>>y2;
        for(int dy=y;dy<y2;dy++){
            for(int dx=x;dx<x2;dx++)
                matrix[dy][dx]=1;
        }
    }
    
    for(int y=0;y<n;y++){
        for(int x=0;x<m;x++){
            if(!matrix[y][x]&&!visited[y][x]){
                v.push_back(0); dfs(x,y,v.size()-1);
            }          
        }
    }
    
    sort(v.begin(), v.end());
    int ans=v.size(); cout<<ans<<endl;
    for(int i=0;i<ans;i++)
        cout<<v[i]<<" ";    
}