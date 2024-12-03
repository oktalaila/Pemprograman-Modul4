#include <stdio.h>

int main (){
    int a, b;
    scanf("%d %d", &a, &b);
    int x=a, y=b;
    while(1) {
        printf("%d %d", x, y);
        if(x==b && y==a) break;
        if(a > b){x--; y++;}
        else{x++; y--;}
        printf(" - ");
    }
}