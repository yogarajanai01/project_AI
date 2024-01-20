# include<stdio.h>
#include<stdlib.h>

int oddoreven()
{
    int a;
    printf("Enter the value of a =");
    scanf("%d",&a);
      
    if (a%2==0)
    {
        printf("EVEN Number");
    }
    else 
    {
        printf("ODD Number");
    }
    
    return 0;
}


