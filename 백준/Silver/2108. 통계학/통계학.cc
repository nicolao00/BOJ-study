#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
using namespace std;
int often[2]={9999,9999};
int num[8001] = {0,};
vector<int> v;

int main(){
    int size;
    cin >> size;
    for(int i=0;i<size;i++){
        int temp; cin>> temp;
        v.push_back(temp);
        if(temp<0) num[4000 + temp*-1]++;
        else num[temp]++;
    }
    sort(v.begin(), v.end());
    double sum = accumulate(v.begin(), v.end(), 0);
    
    if(round(sum/size) == -0) cout <<"0\n";
    else cout << round(sum/size) << "\n";
    
    cout << v[size/2] << "\n";

    int max = 0;
    for (int i = 4000; i >= 0; i--)
    {
        if (max < num[i])
        {
            often[0] = i;
            often[1] = i;
            max = num[i];
        }
        else if (max == num[i] && max != 0)
        {
                often[0] = often[1];
                often[1] = i;
        }
    }
    for (int i = 4001; i < 8001; i++)
    {
        if (max < num[i])
        {
            often[0] = 4000 - i;
            often[1] = 4000 - i;
            max = num[i];
        }
        else if (max == num[i] && max != 0)
        {
                often[0] = often[1];
                often[1] = 4000 - i;
        }
    }
    
    cout << often[0] <<"\n";
    if (v[size-1] - v[0] < 0) cout << (v[size-1] - v[0])*-1 << "/n";
    else cout << v[size-1] - v[0] << "\n";
}