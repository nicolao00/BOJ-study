#include <iostream>
#include <algorithm>
using namespace std;

int maxCandy=1;
int N;
char arr[50][50];

int check(){
    int count=1;
    for(int i=0;i<N;i++){
        count=1;
        for(int j=0;j<N-1;j++){
            if(arr[i][j]==arr[i][j+1]) count++;
            else {maxCandy=max(maxCandy,count); count=1;}
        }maxCandy=max(maxCandy,count);
    }
    
    for(int i=0;i<N;i++){
        count=1;
        for(int j=0;j<N-1;j++){
            if(arr[j][i]==arr[j+1][i]) count++;
            else {maxCandy=max(maxCandy,count); count=1;}
        }maxCandy=max(maxCandy,count);
    } return maxCandy;
}

int main(){ 
    cin>>N; string str;  
    for(int i=0;i<N;i++){
        cin>>str; 
        for(int k=0;k<N;k++) 
            arr[i][k]=str[k];
    }

    int ans=0;
    for(int i=0; i<N; i++)
        for (int j = 0; j < N - 1; j++)
        {
            swap(arr[i][j], arr[i][j + 1]);
            ans = max(ans, check());
            swap(arr[i][j], arr[i][j + 1]);
            
            swap(arr[j][i], arr[j + 1][i]);
            ans = max(ans, check());
            swap(arr[j][i], arr[j + 1][i]);        
        }
    cout<<ans;
}