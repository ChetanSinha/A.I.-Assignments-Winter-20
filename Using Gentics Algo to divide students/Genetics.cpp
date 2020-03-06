#include<stdio.h>
#include<stdlib.h>
void mutation(int n,int a1[][n],int a2[][n],int a3[][n]){

    int k,a,l;
    int temp1,temp2,temp;
    for(k=25;k<45;k++){
    a=rand()%25;
    temp1=rand()%100;
    temp2=rand()%100;
    for(l=0;l<100;l++){
        a3[k][l]=a3[a][l];
        a2[k][l]=a2[a][l];
        a1[k][l]=a1[a][l];
    }
    temp=a1[a][temp1];
    a1[a][temp1]=a1[a][temp2];
    a1[a][temp2]=temp;

    temp=a2[a][temp1];
    a2[a][temp1]=a2[a][temp2];
    a2[a][temp2]=temp;

    temp=a3[a][temp1];
    a3[a][temp1]=a3[a][temp2];
    a3[a][temp2]=temp;
   }

 }
 void crossover(int n,int a1[][n],int a2[][n],int a3[][n]){
    int x1,x2,m,o;
    int gene1,gene2;
    int a41[100][n];
    int a42[100][n];
    int a43[100][n];
    for(n=35;n<50;n++){
    x1=rand()%25;
    x2=rand()%25;
    gene1=rand()%100;
    gene2=rand()%100;
    for(o=0;o<100;o++){
        a3[n][o]=a3[x1][o];
        a2[n][o]=a2[x1][o];
        a1[n][o]=a1[x1][o];
        a3[n+15][o]=a3[x2][o];
        a2[n+15][o]=a2[x2][o];
        a1[n+15][o]=a1[x2][o];
    }


        if(gene1>gene2){
            for(m=gene2;m<gene1;m++){
                a41[x1][m]=a1[x1][m];
                a42[x1][m]=a2[x1][m];
                a43[x1][m]=a3[x1][m];

            }
            for(m=gene1;m<gene2;m++){
                a1[x1][m]=a1[x2][m];
                a2[x1][m]=a2[x2][m];
                a3[x1][m]=a3[x2][m];

            }
            for(m=gene1;m<gene2;m++){
                a1[x2][m]=a41[x1][m];
                a2[x2][m]=a42[x1][m];
                a3[x2][m]=a43[x1][m];

            }

        }
        if(gene1<gene2){
            for(m=gene1;m<gene2;m++){
                a41[x1][m]=a1[x1][m];
                a42[x1][m]=a2[x1][m];
                a43[x1][m]=a3[x1][m];

            }
            for(m=gene1;m<gene2;m++){
                a1[x1][m]=a1[x2][m];
                a2[x1][m]=a2[x2][m];
                a3[x1][m]=a3[x2][m];

            }
            for(m=gene1;m<gene2;m++){
                a1[x2][m]=a41[x1][m];
                a2[x2][m]=a42[x1][m];
                a3[x2][m]=a43[x1][m];

            }

        }
 }
 }
 void selection (int n,int a1[][n],int a2[][n],int a3[][n],int marks[]){
 int i,best=301,min1=100,min2=100,min3=100,max1=0,max2=0,max3=0,bestid,j;
 for(i=0;i<50;i++){
 min1=100;
 min2=100;
 min3=100;
 max1=0;
 max2=0;
 max3=0;
    for(j=0;j<n;j++){
        if(a1[i][j]==1){
            if(marks[j]>max1)
                max1=marks[j];
            if(marks[j]<min1)
                min1=marks[j];
        }
        else if(a2[i][j]==1){
            if(marks[j]>max2)
                max2=marks[j];
            if(marks[j]<min2)
                min2=marks[j];
        }
        else if(a3[i][j]==1){
            if(marks[j]>max3)
                max3=marks[j];
            if(marks[j]<min3)
                min3=marks[j];
        }
    }
    if(best>max1+max2+max3-min1-min2-min3){
        best=max1+max2+max3-min1-min2-min3;
        bestid=i;
    }
 }
 printf("\n%d \nGroup 1 : ",best);
 for(i=0;i<n;i++){
    if(a1[bestid][i]==1)
        printf("%d ",marks[i]);
 }
 printf("\nGroup 2 : ");
 for(i=0;i<n;i++){
    if(a2[bestid][i]==1)
        printf("%d ",marks[i]);
 }
 printf("\nGroup 3 : ");
 for(i=0;i<n;i++){
    if(a3[bestid][i]==1)
        printf("%d ",marks[i]);
 }
 printf("\n");
 }
int main(){

    int n,k,j,i,a,x=5;
    printf("Enter Value of n:")
    scanf("%d",&n);
    int a1[100][n];
    int a2[100][n];
    int a3[100][n];
    int marks[n];
    for(j=0;j<25;j++){
        for(i=0;i<n;i++){
            a=rand()%3;
            if(a==0){
                a1[j][i]=1;
                a2[j][i]=0;
                a3[j][i]=0;
            }
            if(a==1){
                a1[j][i]=0;
                a2[j][i]=1;
                a3[j][i]=0;
            }
            if(a==2){
                a1[j][i]=0;
                a2[j][i]=0;
                a3[j][i]=1;

            }
        }
    }
    for(i=0;i<n;i++){
           marks[i]=rand()%101;
        }
        while(x--){
            mutation(n,a1,a2,a3);
        }
        x=5;
        while(x--){
        crossover(n,a1,a2,a3);
        }

        selection(n,a1,a2,a3,marks);

return 0;
}
