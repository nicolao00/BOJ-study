#include <iostream>
#include <string>
using namespace std;

int main()
{
    int arr[13];
    int month, date;
    int sum;
    string day[7];
    arr[0]=0;
    for(int i=1;i<13;i++){
        if(i<8){
            if(i==2) {arr[i]=28; continue;}
            if(i%2==1) arr[i]=31;
            else arr[i]=30;
        }
        else{
            if(i%2==1) arr[i]=30;
            else arr[i]=31;
        }
    }
    cin>>month>>date;
    for(int i=1;i<month;i++) sum+=arr[i];
    day[0]="MON"; day[1]="TUE"; day[2]="WED"; day[3]="THU"; day[4]="FRI";
    day[5]="SAT"; day[6]="SUN";
    sum+=date; sum-=1; sum%=7;
    cout<<day[sum];
}