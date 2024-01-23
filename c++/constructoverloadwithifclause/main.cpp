#include <iostream>

using namespace std;

class namecheck
{

public:

    void name()
    {
    string name;
    cout << "\nEnter your Name: ";
    cin >> name;
    cout << name  << " OK You go further...";
    }
};

class agecheck{

public:

    int age()
    {
        int age;
        cout << "\nEnter your age..";
        cin >> age;

            if (age==20)
            {
                cout << "\nYou are Eligible.. Go further.";
            }
            else
            {
            cout << "\nYou're not Eligible.. Get Out.";
            }
    }
};

class degreecheck{

public:

       int degree()
       {
           int d;
           cout << "\nEnter your degree..";
           cin >> d;

           if(d==1)
           {
               cout << "\nYou're Eligible.";
           }
           else
           {
               cout << "\nYou're not eligible.";
           }
       }
};

int main()
{
         degreecheck dc;
          dc.degree();

          namecheck nc;
          nc.name();

          agecheck ac;
          ac.age();


    return 0;
}
