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
         cout << "Enter your name\t";
         cin >> cons_name;
         cout << cons_name<< "\tYou have the list of tata cars , Right.";
         cout << "\n\tTiago-a\n\tPunch-b\n\tNano-c\n\tHarrier-d\n\tAltroz-e\n\tNexon-f\n\tSafari-g\n\tTigor-h\n\tNexon EV-i\n\tTiagoNRG-j\n";
     }
     void carName()
     {
         char cno;
         string carname;
         cout << "\n Enter the car Name:\t ";
         cin >> carname;
         cout << "enter the letter\t";
         cin >> cno;
         switch(cno)
             {
         case 'a':
                cout << "TATA TIAGO\t" << "sharp hatchback\t" << " cheapest model\t";
                break;
         case 'b':
                 cout << "TATA PUNCH\t" << " best-selling models\t" << " CNG-powered version\t ";
                 break;
         case 'c':
                 cout << "TATA NANO\t" << " world's cheapest car\t" << " ₹ 2.36 to 3.35 Lakh.\t";
                 break;
         case 'd':
                 cout << "TATA HARRIER\t" << "a 5-seater SUV that rivals the MG Hector and Jeep Compass.\t" << "facelift looks bolder, gets smarter tech, and more premium creature comforts.\t";
                 break;
         case 'e':
                 cout << "TATA ALTROZ\t" << " Tigor is the only sedan in the line-up.\t" << "e gold standard of hatchbacks. It has it all – Style, Safety, Performance and Technology ...\t";
                 break;
         case 'f':
                cout << "TATA NEXON\t" << "first crossover SUV\t" << "better options in the subcompact SUV space.\t ";
                break;
         case 'g':
                cout << "TATA SAFARI\t" << "premium luxury with its opulent interiors,Plush Upholstery & advanced infotainment system\t" << "Offering a rugged blend of luxury and capability \t";
                break;
         case 'h':
                cout << "TATA TIGOR\t" << " is the only sedan in the line-up.\t" << " rated safety, stylish design, spacious and comfortable cabin, diesel and EV powertrains, and lastly, for the amount of new .\t";
                break;
         case 'i':
                cout << "TATA NEXON - EV\t" << "Tata Nexon EV Max review - useful real-world range tested!\t" << "31.24 cm Cinematic Touchscreen by HARMAN™ · 9 Speakers · 26.03 cm HD fully reconfigurable Instrument Cluster · 6 Airbags.\t";
                break;
         case 'j':
                cout << "TATA TIAGO NRG\t" << " beefy-looking hatchbacks\t" << " base model starts at Rs. 6.70 Lakh and the top model price goes upto Rs. 8.64 Lakh\t";
                break;
         default:
                break;
             }
     }
};

int main()
{
    car c;
    c.brandname();
    c.carName();
    return 0;
}
/*
#include <iostream>

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
    s.dad();
    s.mom();
    return 0;
}*/
