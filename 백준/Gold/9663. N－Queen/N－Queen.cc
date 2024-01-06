#include <iostream>
using namespace std;

int matrix[15][15], MAX, count=0;
void dfs(int y){
    if(y==MAX) {count++; return;}
    
    for(int i=0;i<MAX;i++){
        if(!matrix[y][i]){
            int lX=i-1, rX=i+1;
            for(int dy=y+1;dy<MAX;dy++){
                if(lX>=0){matrix[dy][lX]++; lX-=1;}
                if(rX<MAX){matrix[dy][rX]++; rX+=1;}
                matrix[dy][i]++;
            }
            dfs(y+1);
            lX=i-1, rX=i+1;
            for(int dy=y+1;dy<MAX;dy++){
                if(lX>=0){matrix[dy][lX]--; lX-=1;}
                if(rX<MAX){matrix[dy][rX]--; rX+=1;}
                matrix[dy][i]--;
            }
        }
    }
}

int main(){
    cin>>MAX; dfs(0); cout<<count;
}