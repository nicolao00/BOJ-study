#include <iostream>
#include <string>

using namespace std;
int main(){
    
int arr[26] = {0,};
string str;
cin >> str;
for (char c:str) {
    if ('a' <= c && c <= 'z')
        arr[c - 'a']++;
    if ('A' <= c && c <= 'Z')
        arr[c - 'A']++;
}

int max=arr[0];
int idx=0;
int same=0;
   for(int i=1;i<26;i++){
       if (max==arr[i]) same++;
       else if (max<arr[i]){ max=arr[i]; idx=i; same=0; }
   }
   if(same!=0) cout<<"?";
   else cout<<(char)('A'+(char)idx);
}