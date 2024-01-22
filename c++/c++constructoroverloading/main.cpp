#include <iostream>

using namespace std;

class constructorsample
{
public:

   constructorsample()
    {
        cout << "Welcome Yogarajan K\n" ;
    }
   constructorsample1()
    {
        cout << "This is first constructor\n";
    }
   constructorsample2()
    {
        cout << "This is second constructor\n";
    }
   constructorsample3()
    {
        cout << "This is third constructor\n";
    }
    constructorsample4()
    {
        cout << "This is fourth constructor\n";
    }
    constructorsample5()
    {
         cout << "This is fifth constructor\n";
    }
    constructorsample6()
    {
         cout << "This is sixth constructor\n";
    }

};

int main()
{
      constructorsample cs;
    cs.constructorsample::constructorsample3();
      return 0;
}
