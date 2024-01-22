#include<stdio.h>
#include<stdlib.h>

int main()
{
    int i;                                    
    int j;                                    

    for ( i=0; i < 10; i++)
    {
       printf("\n#");
       
       for ( j=0; j<i; j++)
       {
        printf("*");
       }
       
    }
    return 0;
}
