#include <iostream>

using namespace std;

class constructorsample
{
public:

   constructorsample()
    {
        cout << "Welcome Yogarajan K\n" ;
    }
   constructorsample( int a)
    {
        cout << "This is first constructor\n";
    }
   constructorsample( int a1,int a2)
    {
        cout << "This is second constructor\n";
    }
   constructorsample(int b1,int b2,int b3)
    {
        cout << "This is third constructor\n";
    }
};

int main()
{
      constructorsample cs;
      constructorsample cs1(1);
      constructorsample cs2(1,2);
      constructorsample cs3(1,2,3);

      return 0;
}
