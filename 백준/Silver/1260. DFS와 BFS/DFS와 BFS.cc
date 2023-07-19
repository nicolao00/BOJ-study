#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<int> graph[1001];
queue<int> que;
bool visited[1001], visitedB[1001];

void dfs(int start){
    visited[start]=true;
    cout<<start<<" ";
    for(int i=0;i<graph[start].size();i++){
        if(!visited[graph[start][i]]) dfs(graph[start][i]);
    }
}

void bfs(int start){
    que.push(start);
    while(que.size()!=0){
        int head=que.front();
        cout<<head<<" ";
        visitedB[head]=true;
        que.pop();
        
        for(int i=0;i<graph[head].size();i++){
            if(!visitedB[graph[head][i]]) {
                que.push(graph[head][i]); visitedB[graph[head][i]]=true;
            }            
        }
    }
}

int main(){
    int nodeSize, branchSize, startNode; 
    cin>>nodeSize>>branchSize>>startNode;
    
    for(int i=0;i<branchSize;i++){
        int start,end; cin>>start>>end;
        graph[start].push_back(end);
        graph[end].push_back(start);
    } 
    
    for(int i=1;i<=nodeSize;i++)
        sort(graph[i].begin(),graph[i].end());
        
    dfs(startNode); cout<<endl; bfs(startNode);
}