//2:34
#include <iostream>
#include <vector>
using namespace std;

int main(){
    int treeNum, needlen; 
    vector<int> tree;
    cin>>treeNum>>needlen;
        
    int temp, maxTree=0, minTree=0;
    for(int i=0;i<treeNum;i++){
        cin>>temp; tree.push_back(temp);
        if(maxTree<temp) maxTree=temp;
    }
    long long int standard=0,total=0;
    int result=0;
    while(maxTree>=minTree){
        total=0;
        standard=(maxTree+minTree)/2;
        for(int i=0;i<treeNum;i++){
            if(standard<tree[i]) total=total+tree[i]-standard;
        }
        /*if(total>needlen) minTree=standard;
        else if(total<needlen) maxTree=standard;
        else break;*/
        if(total<needlen) {
            maxTree = standard -1;
        } else {
            result = standard;
            minTree = standard +1;
        }
    }
    cout<<result;
}