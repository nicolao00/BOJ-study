#include <iostream>
#include <vector>
using namespace std;

int main(){
    cin.tie(NULL); ios::sync_with_stdio(false);
    int n,m; cin>>n>>m;
    vector<int> sum;
    sum.push_back(0);
    for(int i=1;i<=n;i++){
        int temp; cin>>temp;
        sum.push_back(sum[i-1]+temp);
    }
    
    for(int i=0;i<m;i++){
        int start, end;
        cin>>start>>end;
        cout<<sum[end]-sum[start-1]<<'\n';
    }
}