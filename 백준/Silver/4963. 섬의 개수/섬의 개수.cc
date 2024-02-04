#include <iostream>
#include <cstring>
#define MAX 51
using namespace std;

int matrix[MAX][MAX];
int visited[MAX][MAX];
int x[8]={-1,0,1,-1,1,-1,0,1}, y[8]={-1,-1,-1,0,0,1,1,1};

void dfs(int row, int col){
    if(visited[row][col]) return;
    
    visited[row][col]=1;
    for(int i=0;i<8;i++){
        if(matrix[row+x[i]][col+y[i]]&&!visited[row+x[i]][col+y[i]]) dfs(row+x[i],col+y[i]);
    }
}
    

int main(){
    while(1){
        int col, row; cin>>col>>row;
        if(col==0 && row==0) break;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                int temp; cin>>temp; matrix[i][j]=temp;
            }
        }
        int count=0;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(matrix[i][j]){
                    if(visited[i][j]==0) {count++; dfs(i,j);}
                }
            }
        } cout<<count<<endl;
            
        for(int i=0;i<row;i++){memset(matrix[i],0,sizeof(int)*MAX); memset(visited[i],0,sizeof(int)*MAX);}        
    }
}