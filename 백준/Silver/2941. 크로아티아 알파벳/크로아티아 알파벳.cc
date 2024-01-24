#include <iostream>
using namespace std;

int main(){
    string str; 
    cin>>str;
    int word=str.size();    // 입력 문자열의 길이
    int changeW=word; // 크로아티아 수
    // 크로아티아 알파벳 찾기 (찾으면 그만큼 길이에서 뺴기)
    for(int i=0;i<word;i++){
        if(str[i]=='-') {
            if(str[i-1]=='c') changeW--;
            if(str[i-1]=='d') changeW--;
        }
        if(str[i]=='='){
            if(str[i-1]=='s') changeW--;
            if(str[i-1]=='z'){
                if(str[i-2]=='d') changeW-=2;
                else changeW--;
            }
            if(str[i-1]=='c') changeW--;
        }
        if(str[i]=='j'){
            if(str[i-1]=='l') changeW--;
            if(str[i-1]=='n') changeW--;
        }
    } cout<<changeW;
} 