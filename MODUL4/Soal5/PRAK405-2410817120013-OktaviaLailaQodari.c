#include <stdio.h>

int main (){
    int i, a, b, hasil;
    int c = 0;

    scanf("%d %d", &a, &b); 

    for (i = 1; i <= a; i ++){
        hasil = 0;
        for(int j = i; j>0; j--){
            printf("(%d*%d)", j,b);
            hasil += j*b; 
            c += j*b;
            (j>1)? printf(" + "): printf(" = %d", hasil);
        }
        printf("\n");
    }
    printf("%d", c);
}