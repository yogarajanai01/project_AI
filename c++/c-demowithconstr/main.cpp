
#include <iostream>
using namespace std;

class classandobjectsfirstsample
{
    public:
    int a=1;

void multiply()
    {
        int x,y,z;
        cout << "\nEnter value x :\n";
        cin >> x;
        cout <<"\nEnter value y :\n";
        cin >> y;
        cout <<"\nMultiplied value z :\n"<<(x*y);
    }

void Addition ()
{
    int c,b,d;
    cout << "\nEnter c :\n";
    cin >> c;
    cout << "\nEnter b :\n";
    cin >> b;
    d = c + b;
    cout << "\nAdded value D is:\n" << d;

}
void subtraction()
{
int e,f,g;
cout <<  "\nEnter e :\n";
cin >> e;
cout << "\nEnter f :\n";
cin >> f;
g = f - e;
cout << "\nSub Value G is:\n" << g;
}
void division()
{
    int h,i;
    cout << "\nEnter the value h:\n";
    cin >> h;
    cout << "\nEnter the value i:\n";
    cin >> i;
    cout << "\ndivided value is :\n" << i/h;
}
void modulus()
{
    int j,k;
    cout << "\nEnter the value j:\n";
    cin >> j;
    cout << "\nEnter the value k:\n";
    cin >> k;
    cout << "\nValue for  modulus is :\n" << j%k;

}
void increment()
{
    int inc;
    cout << "\nEnter the value for inc :\n";
    cin >> inc;
    cout << "\n The Incremented Value is :\n" << ++inc;
}
void decrement()
{
    int dec;
    cout << "\nEnter the value for dec :\n";
    cin >> dec;
    cout << "\n The Decremented Value is :\n" << --dec;
}
};

int main()
{

    classandobjectsfirstsample COFS;
    COFS.Addition();
    COFS.subtraction();
    COFS.multiply();
    COFS.division();
    COFS.modulus();
    COFS.increment();
    COFS.decrement();
    return 0;
}



























