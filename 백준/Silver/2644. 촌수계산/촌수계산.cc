//2154
#include <iostream>
#include <vector>
#define MAX 101
using namespace std;

int matrix[MAX][MAX], visited[MAX];
int peopleSize; int ans;

void dfs(int start, int find, int reach){
    visited[start]=1;
    
    for(int i=0;i<=peopleSize;i++){
        if(matrix[start][i]==1&&!visited[i]){
            int temp=reach; temp++; visited[i]=1;
            if(i==find) {if(ans==0) ans=temp; else if(ans>reach) ans=temp;}
            else dfs(i,find,temp);
        }            
    }
}

int main(){
    int findA,findB, branchSize;
    cin>>peopleSize>>findA>>findB>>branchSize;
    for(int i=0;i<branchSize;i++){
        int a,b; cin>>a>>b;
        matrix[a][b]=matrix[b][a]=1;
    } 
    dfs(findA,findB,0); 
    if(ans) cout<<ans;
    else cout<<"-1";
}