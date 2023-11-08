#define MAX 26
#include <iostream>
#include <algorithm>
#include <vector> // 단지수 저장
using namespace std;
int map[MAX][MAX], visited[MAX][MAX];
int x[4]={0,1,0,-1}, y[4]={-1,0,1,0};
vector<int> v;

void dfs(int h,int w){
    int top=v.size();
    v[top-1]++;
    visited[h][w]=1;
    
    for(int i=0;i<4;i++){
        if(map[h+y[i]][w+x[i]]&&!visited[h+y[i]][w+x[i]])
            dfs(h+y[i],w+x[i]);
    }
}

int main(){
    int wid; cin>>wid;
    for(int i=0;i<wid;i++){
        for(int j=0;j<wid;j++){
            scanf("%1d", &map[i][j]); // stdio.h
        }
    }
    
    for(int i=0;i<wid;i++){
        for(int j=0;j<wid;j++){
            if(map[i][j]&&!visited[i][j]){
                v.push_back(0); dfs(i,j);
            }
        }
    }
    sort(v.begin(),v.end()); cout<<v.size()<<endl;
    for(int i=0;i<v.size();i++)
        cout<<v[i]<<endl;
    
}