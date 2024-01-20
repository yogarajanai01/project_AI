#include <iostream>

using namespace std;

class construct
{
public:

    void yogarajan()
    {
    int A,B;
    cout << "\n ADDITION " << "\n Enter value A =" ;
    cin  >> A;
    cout << "\n Enter value B =";
    cin  >> B;
    cout << "\n ADDED VALUE IS " << A+B;
    }
    void yogarajan(int c)
    {
        cout  << "\n Enter value for c:\t" << c*c;
    }
 void yogarajan(string initial,string name)
    {
        cout  << "\n Enter value for concat:\t" << initial + name;
    }
void yogarajan(float a,float b,float c)
{
    cout << "\n The Value of Float is :\t" << a+b+c;
}
};


int main()
{
construct ctr;
ctr.yogarajan();
ctr.yogarajan(10);
ctr.yogarajan("K.","yogarajan");
ctr.yogarajan(10.5,15.8,20.5);
return 0;
}
