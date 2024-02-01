#include <iostream>
using namespace std;
int N,M, arr[9];
bool visited[9];

void dfs(int len){
    if(len==M){
        for(int i=0;i<M;i++)
            cout<<arr[i]<<' ';
        cout<<'\n';
    }
    else{
        int start=1;
        if(len>0) start=arr[len-1];
        
        for(int i=start;i<=N;i++){
            if(!visited[i]&&M-len-1<=N-i){                
                visited[i]=true;
                arr[len]=i;
                dfs(len+1);
                visited[i]=false;
            }
        }
    }
}

int main(){
    cin>>N>>M;
    dfs(0);
}
/*
1~N중 M개 고른 수열
3 1(2) = 2(1) 필요한 숫자 개수
N-전꺼값 9-7=2
*/