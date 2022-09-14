#include <iostream>
using namespace std;

int main()
{

    string cars[4] = {"Tesla", "BMW", "Ford", "Audi"};
    cout << "First Car is: " << cars[0] << endl;
    cout << "Fourth Car is: " << cars[3] << endl;

    cars[0] = "MG Hector";
    cout << "Now, First Car is: " << cars[0] << endl;

    return 0;
}