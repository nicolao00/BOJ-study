//2148
#include <iostream>
using namespace std;
int dp[100001]={0,-1,1,-1,2,1,};

int main(){
   int price; cin>>price;
    for(int i=6;i<=price;i++){
        int two=0; int five=0;
        if(dp[i-2]!=-1) two=dp[i-2]+1;
        if(dp[i-5]!=-1) five=dp[i-5]+1;
        if(two==0&&five==0) dp[i]=-1;
        else{
            if(two>five){
                if(five==0) dp[i]=two;
                else dp[i]=five;
            }
            else dp[i]=two;
        }
    } 
   cout<<dp[price];
}

//    f(n)=2+f(n-2) / 5+f(n-5)