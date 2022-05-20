#include <iostream>

using namespace std;

int separate(int num){
    int ten, one;
    ten=num/10; one=num%10;
    return (one*10+((ten+one)%10));
}

int main()
{
    int num, sol;
    int count=0;
    cin>>num;
    sol=num;
    
    while(1){
        sol=separate(sol);
        count++;
        if(sol==num) break;
    }
    cout<<count;
} 