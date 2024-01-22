#include<iostream>

using namespace std;

int main ()
{
    int value1,value2,total;
    cout << "Enter the value1 :";
    cin >> value1;
    cout << "Enter the value2 :";
    cin >> value2;
    total = value1+value2 ;
    cout << "The total value is :" << total;

    return 0;
}



#include <iostream>

using namespace std;

int main()
{
    cout << "Hello world!" << endl;
    cout << "Welcome to c++!" << endl;
    return 0;

}

#include<iostream>
using namespace std;

int main()
{
    int value1,value2,total,sym;
    cout << "Enter the value1 :";
    cin >> value1;
    cout << "Enter the value2 :";
    cin >> value2;
    cout << "Enter the operator:";
    cin >> sym;

    switch(sym)
    {
    case 1:
        total = value1+value2;
        cout << "Added value is :"<<total;
        break;

    case 2:
        total = value1-value2;
        cout << "Subtracted value is :"<<total;
        break;

    case 3:
        total = value1*value2;
        cout << "Multiplied value is :"<<total;
        break;

    case 4:
        total = value1/value2;
        cout << "Divided value is :"<<total;
        break;

    case 5:
        total = value1%value2;
        cout << "Remainder value is :"<<total;
        break;
    case 6:
        total = value1++;
        cout << "Incremented value is :"<<value1;
        break;


    default :
        break;
    }
 return 0;





}
