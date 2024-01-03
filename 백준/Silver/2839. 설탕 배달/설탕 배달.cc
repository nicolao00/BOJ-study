#include <iostream>

using namespace std;

class Math{
    int three[1000], five[1000], count[1000];
    // 3의 갯수, 5의 갯수, 총 갯수들 
    int num;        // 입력값
    int size;       // N킬로그램이 정확하게 나온 배열 속 원소 갯수
    public:
    void setN(int num);     // 입력값 받는 함수
    void setA();            // 3,5의 갯수를 각 배열에 넣는 함수
    int setC();
    void print();
};

void Math::setN(int num){ this->num=num;}

void Math::setA(){
    int i=0;
    int body=num/5;     // body: 입력받은 수에서 5의 최대갯수
    int extra;    // 5의 최대갯수 뺸 나머지값
    //cout<<"body: "<<body<<endl;
    for(body;body>=0;body--){
        extra=num-5*body;
        if(extra%3==0) {three[i]=extra/3; five[i++]=body;}
        else continue;
    } size=i; //cout<<"setA size: "<<size<<endl;
}

// 임의의 인덱스속 원소의 갯수를 저장하는 배열 셋팅하고 최솟값 구해서 반환하는 함수
int Math::setC(){
    if(size==0) return -1;
    
    for(int i;i<size;i++) count[i]=three[i]+five[i];
    int temp;
    temp=count[0];
    for(int i=0;i<size;i++){
        if(temp>count[i]) temp=count[i];
    }
    return temp;
}

void Math::print(){
    cout<<num<<" "<<size<<endl;
    for(int i=0;i<size;i++) cout<<three[i]<<" "<<five[i]<<endl;
}


int main()
{
    int num;
    cin>>num;
    Math a;
    a.setN(num);
    a.setA();
    //a.print();
    cout<<a.setC();
}