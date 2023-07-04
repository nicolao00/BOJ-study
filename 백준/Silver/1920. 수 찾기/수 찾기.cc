#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> numArr;
vector<int> ans;
int idx=0;

int midSearch(int begin,int end){
    if(ans[idx]<numArr[begin]||ans[idx]>numArr[end]) {cout<<"0"<<"\n"; return -1;}
     
    while(begin<=end){
        int flag=(end+begin)/2;
        if(ans[idx]<numArr[flag]) end=flag-1;
        else if(ans[idx]==numArr[flag]) {cout<<"1"<<"\n"; return 0;}
        else if(ans[idx]>numArr[flag]) begin=flag+1;
    } cout<<"0"<<"\n"; return 0;
}    

int main(){
    int size; cin>>size; 
   
    for(int i=0;i<size;i++){
        int num; cin>>num; numArr.push_back(num);
    } 
    
    int ansSize; cin>>ansSize;
    for(int i=0;i<ansSize;i++){
        int num; cin>>num; ans.push_back(num);
    }    sort(numArr.begin(),numArr.end());
    
    for(int i=0;i<ansSize;i++){
        midSearch(0,size-1); idx++;
    }
}