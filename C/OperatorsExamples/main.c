#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=10;
    int b=20;
    int c;
    AdditionProgram(a,b);
    SubtractionProgram(a,b);
    MultiplicationProgram(a,b);
    DivisionProgram();
    ModulusProgram(150,3);
    IncrementProgram(20);
    DecrementProgram(b);
    AssignmentDemoOperatorsProgram(a,b);
    ComparisonOperatorsProgram();
    logicalOperatorsProgram();
    return 0;
}
int AdditionProgram(int a,int b)
{
    int c=a+b;
    printf("\n\tADDITION:\n\n");
    printf("\tThe FirstValue is:%d\n\tThe SecondValue is:%d\n\tThe Value of Addition is:%d\n",a,b,c);

}
int SubtractionProgram(int a,int b)
{
    int c=b-a;
    printf("\n\tSUBTRACTION:\n\n");
    printf("\tThe A is:%d\n\tThe B is:%d\n\tThe Value of Subtraction is:%d\n",a,b,c);

}
int MultiplicationProgram(int a,int b)
{
   int c=a*b;
    printf("\n\tMultiplication:\n\n");
    printf("\tThe A is:%d\n\tThe B is:%d\n\tThe Value of Multiplication is:%d\n",a,b,c);

}
int DivisionProgram()
{
    int d=15;
    int e=3;
    int c=d/e;
    printf("\n\tDivision:\n\n");
    printf("\tThe D is:%d\n\tThe E is:%d\n\tThe Value of Division is:%d\n",d,e,c);

}
int ModulusProgram(int x,int y)
{
    int c=x%y;
    printf("\n\tModulus:\n\n");
    printf("\tThe X is:%d\n\tThe Y is:%d\n\tThe Value of Modulus is:%d\n",x,y,c);
}
int IncrementProgram(int z)
{
    while(z<25)
    {
        printf("\n\t The value for the increment program is....%d\n\n",z++);
    }
}
int DecrementProgram(int b)
{
 while(b>10)
    {
        printf("\n\t The value for the Decrement program is....%d\n",b);
        b--;
    }
}
int AssignmentDemoOperatorsProgram(int a,int b)
{
     int c,d,e,f,g;
     c=a;
    c+=a;
    b-=a;
    a*=c;
    b/=c;
    printf("\n\tThe value of ASSIGNMENT operator is:%d\n\tThe value of += operators is:%d\n\tThe value of -= operators is:%d\n\tThe value of *= operators is:%d\n\tThe value of /= operator is:%d\n\n",c,c,b,a,c);
    return 0;
}
int ComparisonOperatorsProgram()
{
  int a=10;
  int b=20;
  int c=30;
  int d,e,f,g,h,i;
    d=c>a;
    e=c<b;
    f=a>=b;
    g=c<=a;
    h=a!=b;
    i=a==b;
    printf("\n\tThe COMPARISON operators program are follows:\n\tThe value of greater than is:%d\n\tThe Value of less than is:%d\n\tThe Value of greater than or Equal to is:%d\n\tThe value of less than or equal to is:%d\n\tThe value of not equal to is:%d\n\tThe value of double equal to is:%d\n",d,e,f,g,h,i);
    return 0;
}
int logicalOperatorsProgram()
{
    printf("LOGICAL OPERATORS PROGRAM:");
     int a=0;
    if(a>10 && 10<a)
{
    printf("\n\tThe logical AND Operation is true.\n");

}
else if (a==11 || a>10)
{
    printf("\n\tThe logical OR operations is true.\n");
}
else if (a!=10)
{
    printf("\n\tThe logical NOT operators is true.\n");
}
else
{
    printf("\n\tNO VALUE IS TRUE.\n");
}
}
