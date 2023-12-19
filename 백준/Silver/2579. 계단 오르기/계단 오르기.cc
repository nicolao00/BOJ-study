#include <iostream>
using namespace std;

int main()
{
    int step[303] = {0,}, dp[303][2] = {0,};
    int size; cin >> size;
    
    for (int i = 1; i <= size; i++)
        cin >> step[i];

    dp[1][0]=step[1];
    dp[2][0]=step[2]; dp[2][1]=step[2] + dp[1][0];
    for(int i = 3; i<=size; i++){
        dp[i][0] = step[i] + ((dp[i - 2][1] > dp[i - 2][0]) ? dp[i - 2][1] : dp[i - 2][0]);
        dp[i][1] = step[i] + dp[i - 1][0];
    }
    int ans = (dp[size][0] > dp[size][1]) ? dp[size][0] : dp[size][1];
    cout << ans;
}