#include <iostream>
using namespace std;

class Info{
    int weight, height, bigC, rate;    //몸무게, 키, 몇명보다 크다, 덩치 등수
    public:
    Info(int weight=0, int height=0, int bigC=0)
    :weight(weight),height(height), bigC(bigC){}
    
    void setInfo(int weight, int height){
        this->weight=weight; this->height=height;
    }
    int getW(){return weight;}
    int getH(){return height;}
    int getC(){return bigC;}
    int getR(){return rate;}
    void plus(){bigC++;}
    void setR(int r){rate=r;}
};

int main()
{
    int pNum, weight, height; 
    cin>>pNum;
    
    Info* a = new Info[pNum];
    
    for(int i=0;i<pNum;i++){
        cin>>weight>>height;
        a[i].setInfo(weight,height);
    }
    for(int i=0;i<pNum;i++){
        for(int j=i+1;j<pNum;j++){
            if(a[i].getW()>a[j].getW()&&a[i].getH()>a[j].getH()) a[j].plus();
            if(a[i].getW()<a[j].getW()&&a[i].getH()<a[j].getH()) a[i].plus();
        }
    }
    
    for(int i=0;i<pNum;i++){
        cout<<a[i].getC()+1<<' ';
    }
}