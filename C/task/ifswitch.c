#include<stdio.h>
#include<stdlib.h>

int main()
{
    int y;
    printf("Enter the value =");
    scanf("%d",&y);
    
   if (y==2)
    {
     
         int a,b;
         char x;
         printf("\n enter the value of a =");
        scanf("%d",&a);
        printf("\n enter the value of b =");
        scanf("%d",&b);
       printf("\nselect the operators =");
        scanf(" %c",&x); 
     
        switch (x)
     {
        int c;
        case '+':
        c=a+b;
        printf ("added value is :%d",c);
        break;    
        case '-':
        c=a-b;
        printf ("subtracted value is :%d",c);
        break;
        case '*':
        c=a*b;
        printf ("Multiplied value is :%d",c);
        break;
        case '/':
        c=a/b;
        printf ("divided value is :%d",c);
        break;

        }
    }
    else
    {
        int a1,b1,d1;
        char x;
        printf("Enter the value of a1 =");
        scanf("%d",&a1);
        printf("Enter the value of b1 =");
        scanf("%d",&b1);
        printf("Enter the value of d1 =");
        scanf("%d",&d1);
         printf("\nselect the operators =");
        scanf(" %c",&x); 
     
        switch (x)
     {
       int e;
        case '+':
        e=a1+b1+d1;
        printf ("added value is :%d",e);
        break;    
        case '-':
        e=a1-b1-d1;
        printf ("subtracted value is :%d",e);
        break;
        case '*':
        e=a1*b1*d1;
        printf ("Multiplied value is :%d",e);
        break;
        case '/':
        e=a1/b1/d1;
        printf ("divided value is :%d",e);
        break;
     }


    }
    

    return 0;
}
