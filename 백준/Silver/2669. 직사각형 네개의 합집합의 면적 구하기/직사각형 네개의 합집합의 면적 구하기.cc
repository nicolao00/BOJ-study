#include <iostream>
#include <cstring>
using namespace std;
int main()
{
   char chk[100][100];
   memset(chk,0,sizeof(chk));
   
   int minX,minY,maxX,maxY;
   for(int i=0;i<4;i++){
       cin>>minX>>minY>>maxX>>maxY;
       for(int y=minY; y<maxY; y++){
           for(int x=minX; x<maxX; x++) chk[y][x]++;
       }
   }
 
   int sum=0;
   for(int x=0;x<100; x++){
       for(int y=0; y<100; y++){
          if(chk[y][x]!=0) sum++;
       }
   }cout<<sum;
}