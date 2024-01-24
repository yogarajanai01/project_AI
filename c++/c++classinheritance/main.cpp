#include<iostream>

using namespace std;

class car
{
public:
     void brandname()
     {
         string name,cons_name;
         cout << "\n Enter the brandname :\t";
         cin >> name;
         cout << "\n Hii.. This is the brand of car " << name << endl;
         cin >> cons_name;
         cout << cons_name<< "\tYou have the list of tata cars , Right.";
         cout << "\n\tTiago\n\tPunch\n\tNano\n\tHarrier\n\tAltroz\n\tNexon\n\tSafari\n\tTigor\n\tNexon EV\n\tTiago NRG\n";
     }
     void carName()
     {
         string carname;
         cout << "\n Enter the car Name: ";
         cin >> carname;
     }
     void cardetails()
     {
         int a;
         cout << "\n\tTiago-1\n\tPunch-2\n\tNano-3\n\tHarrier-4\n\tAltroz-5\n\tNexon-6\n\tSafari-7\n\tTigor-8\n\tNexon EV-9\n\tTiago NRG-10\n";
         cin >> a;

         switch(a)
         case 1:
             {
             cout << "TATA TIAGO ";
             break;
             }

           /*  case 2:
                 cout << "TATA PUNCH";
                 break;
                 case 3:
                     cout << "TATA NANO";
                     break;
                     case 4:
                         cout << "TATA HARRIER";
                         break;
                         case 5:
                             cout << "TATA ALTROZ";
                             break;
                             case 6:
                                 cout << "TATA NEXON";
                                 break;
                                case 7:
                                    cout << "TATA SAFARI";
                                    break;
                                    case 8:
                                        cout << "TATA TIGOR";
                                        break;
                                        case 9:
                                            cout << "TATA NEXON - EV";
                                            break;
                                           case 10:
                                               cout << "TATA TIAGO NRG";
                                               break;*/

     }
};







int main()
{
    car c;
    c.brandname();
    c.carName();

    return 0;
}






























































































































































































/*#include <iostream>

using namespace std;

class parentfather
{
public:
    void dad()
    {
        cout << "\n ALL MY ASSETS ARE YOURS AFTER ME." << endl;
    }
};

class parentmother
{
public:
    void mom()
    {
        cout << "\n All MY LOVE IS FOR YOU." << endl;
    }
};


class son : public parentfather,public parentmother
{

} ;




int main()
{
    son s;
    //s.dad();
    s.mom();
    return 0;
}*/
