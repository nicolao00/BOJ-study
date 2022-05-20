#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool value(string t){
    string v=t;
    long unsigned int idx=0;

    for(int i=0;i<26;i++){
        idx=t.find('a'+i);
        while(1){
            if(v.find('a'+i)==string::npos) break;
            else if(idx!=v.find('a'+i)) return false;
            else v.erase(v.find('a'+i),1);
        }v=t;
    }return true;
}

int main(){
    vector<string> a;   // 입력받은 변수를 저장할 배열
    string b;           // 입력받을 변수
    int size=0;         // 입력받을 단어 갯수
    int count=0;        // 그룹 단어의 개수
    
    cin>>size;
    for(int i=0;i<size;i++) { 
        cin>>b; a.push_back(b); 
    }
    for(int i=0;i<size;i++) { 
     if(value(a[i])) count++;
    }cout<<count;
}