#include <iostream>
using namespace std;

int main(){
    int n, m, startN=0, startM=0;
    int ans = 64;
    char str[51][51];
    char arr[2] = {'B', 'W'};
    
    cin >> n >> m;
    for(int i=0; i<n; i++)
        cin >> str[i];

    int val = 0;
    while(startN <= n-8){
        if(startM > m - 8){
            startM = 0; 
            startN++; 
            continue;
        }

        for (int arridx = 0; arridx < 2; arridx++)
        {
            val = 0;
            for (int i = 0; i < 8; i++)
            {
                for (int j = 0; j < 8; j++)
                {
                    if (str[startN + i][startM + j] != arr[(startM + i + j + arridx) % 2])
                        val++;
                }
            }
            if (val < ans)
            ans = val;
        }
        startM++;
    }
    cout<<ans;
}