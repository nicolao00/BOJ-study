#define MAX 101
#include <iostream>
using namespace std;
int matrix[MAX][MAX];
int visited[101];
int count=0;

void dfs(int start){
    visited[start]=1;
    for(int i=0;i<MAX;i++){
        if(!visited[i]&&matrix[start][i]) {dfs(i); count++;}
    }
}

int main(){
    int comSize,branchSize; cin>>comSize>>branchSize;
    for(int i=0;i<branchSize;i++){
        int a,b; cin>>a>>b; matrix[a][b]=matrix[b][a]=1;
    } dfs(1); cout<<count;
}