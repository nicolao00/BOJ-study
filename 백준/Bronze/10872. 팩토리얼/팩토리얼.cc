#include <iostream>
using namespace std;

int main(){
    int result = 1;
    int a;
    cin >> a;
    for(int i=a; i>0; i--)
        result *= i;
    cout << result;
}