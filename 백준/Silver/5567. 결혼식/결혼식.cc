#include <iostream>
#include <vector>
#include <queue>
using namespace std;
// bfs로 풀어야하네 

vector<int> v[501];
int visited[501];
int count=0;

void bfs(int start){
    visited[start]=1;
    queue<int> que;

    for(int i=0;i<v[start].size();i++){
        int temp=v[start][i];
        que.push(temp); visited[temp]=1; count++;
    }
    
    while(!que.empty()){
        int headIdx=que.front();
        for(int i=0;i<v[headIdx].size();i++){
            int head=v[headIdx][i]; 
            if(!visited[head]){count++; visited[head]=1;}
        } que.pop();
    }
}

int main(){
    int pSize, lSize; cin>>pSize>>lSize;
    for(int i=0;i<lSize;i++){
        int a, b; cin>>a>>b;
        v[a].push_back(b); v[b].push_back(a); 
    } bfs(1); cout<<count;
}