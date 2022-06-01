#include <iostream>
using namespace std;

int main(){
    int dp[1001][3] = {0,}, house[1001][3]= {0,};
    int size; cin >> size;
    for(int i=1; i<=size; i++){
        for(int j=0;j<3;j++)
            cin >> house[i][j];
    }
    dp[1][0]=house[1][0], dp[1][1]=house[1][1], dp[1][2]=house[1][2];
    for(int i=0;i<3;i++){
        int min=1000001;
        for(int j=0;j<3;j++){
            if(j==i) continue;
            if(min>dp[1][j]) min = dp[1][j];
        } dp[2][i] = min + house[2][i];
    }

    int min, temp, sum;
    for (int i = 3; i <= size; i++){
        for (int thr=0; thr<3; thr++){
            sum = min = 1000001;
            for(int first=0; first<3; first++){
                temp = 1000001;
                for(int sec=0;sec<3;sec++){
                    if(sec == thr || sec == first) continue;
                    if(temp > house[i-1][sec]) temp = house[i-1][sec];
                }
                sum = dp[i-2][first] + temp;
                if(min > sum) min = sum;
            }
            dp[i][thr] = min + house[i][thr];
        }
    }
    min = 1000001;
    for(int i=0;i<3;i++){
        if(min > dp[size][i]) min = dp[size][i];
    } cout<<min;
}