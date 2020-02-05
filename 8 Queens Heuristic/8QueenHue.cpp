#include<iostream>
using namespace std;
int falseCount(int arr[8][8],int row,int column){
    int cnt=0;
    //vartical
    for(int i=0;i<8;i++){
        if(arr[i][column]==1){
            cnt++;
        }
    }
    //digonal1
    for(int i=row-1,j=column-1;i>=0&&j>=0;i--,j--){
        if(arr[i][j]==1){
            cnt++;
        }
    }
    for(int i=row+1,j=column+1;i<=7&&j<=7;i++,j++){
        if(arr[i][j]==1){
            cnt++;
        }
    }
    //diagonal2
    for(int i=row-1,j=column+1;i>=0&&j<=7;i--,j++){
        if(arr[i][j]==1){
            cnt++;
        }
    }
    for(int i=row+1,j=column-1;i<=7&&j>=0;i++,j--){
        if(arr[i][j]==1){
            cnt++;
        }
    }
    return cnt;
}
void print(int arr[8][8]){
    for(int i=0;i<8;i++){
        for(int j=0;j<8;j++){
            cout<<arr[i][j]<<" ";
        }
        cout<<"\n";
    }
    cout<<"\n";
}

void Queen8(int arr[8][8]){
    int row=0,cnt=8,column=0,cnt1;
    for(int i=0;i<8;i++){
        cnt=8;
        for(int j=0;j<8;j++){
            arr[i][j]=0;
            cnt1=falseCount(arr,i,j);
            if(cnt>cnt1){
                cnt=cnt1;
                row=i;
                column=j;
            }
            //cout<<cnt1<<"  ";
        }
        //cout<<"\n";
        arr[row][column]=1;
        row=i+1;
        column=0;
    }
    print(arr);
}

int main(){
    int arr[8][8],row,cnt;
    for(int i=0;i<8;i++){
        for(int j=1;j<8;j++){
            arr[i][j]=0;
        }
    }
    for(int i=0;i<8;i++){
        arr[i][0]=1;
    }
    Queen8(arr);
}
