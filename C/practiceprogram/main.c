#include <stdio.h>
#include <stdlib.h>

int main()
{
   pointer();
   stpointer();
}

int pointer()
{
    int a = 10;
    int *p =&a;
    printf("value of A ...%d\n",a);
    printf("address of A ...%p\n",&a);
    printf("address of A ...%d\n",&a);
    printf("value in address of A ...%d\n",*p);
    return 0;
}

int stpointer()
{
    char myname[100] = "yogarajan is my name" ;
   // scanf("%[^\n]",myname);
    char *q =&myname;
    printf("value of myname...%s\n",myname);
    printf("address of myname ...%p\n",&myname);
    printf("address of myname ...%d\n",&myname);
    printf("value in address of myname ...%s\n",q);
    return 0;
}
