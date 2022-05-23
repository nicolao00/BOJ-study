#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int check[4], num[12], numSize;
vector<int> v;

void dfs(int len, int temp){
    if(len==numSize){ v.push_back(temp); return; }
    else{
        for(int i=0;i<4;i++){
            int value=temp;
            if(check[i]!=0){
                switch(i){
                    case 0:
                        value+=num[len];
                        break;
                    case 1:
                        value-=num[len];
                        break;
                    case 2:
                        value*=num[len];
                        break;
                    case 3:
                        if(value<0){value=value*-1/num[len]*-1;}
                        else value/=num[len];
                        break;
                } check[i]--; dfs(len+1,value); check[i]++;
            }
        }
    }
}

int main(){
    cin>>numSize;
    for(int i=0;i<numSize;i++) cin>>num[i];
    for(int i=0;i<4;i++) cin>>check[i];
    dfs(1,num[0]); sort(v.begin(),v.end());
    cout<<v[v.size()-1]<<'\n'<<v[0];
}