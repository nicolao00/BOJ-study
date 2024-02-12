#include <iostream>
#include <vector>
#include <queue>
#define MAX 100001
using namespace std;
queue<int> que;
vector<int> v[2*MAX];
int visited[2*MAX];

void bfs(int s,int e){
    v[0].push_back(s); int ans=1; visited[s]=1; que.push(s);
    
    while(1){
        while(!que.empty()){
            int num=que.front(); int n1=num-1, n2=num*2, n3=num+1;
            if(n1==e||n2==e||n3==e) {cout<<ans; return;}           
            if(0<=n1&&n1<=2*MAX&&!visited[n1]) {v[ans].push_back(n1); visited[n1]=1;}
            if(0<=n2&&n2<=2*MAX&&!visited[n2]) {v[ans].push_back(n2); visited[n2]=1;}
            if(0<=n3&&n3<=2*MAX&&!visited[n3]) {v[ans].push_back(n3); visited[n3]=1;}
            que.pop(); //ans 올려줘야함
        }
        
        for(int i=0;i<v[ans].size();i++)
            que.push(v[ans][i]);
        ans++;
    }
}

int main(){
    int start,end; cin>>start>>end;
    if(start==end) {cout<<"0"; return 0;}
    bfs(start,end);
}