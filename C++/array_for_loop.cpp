#include <iostream>
using namespace std;

int main()
{

    string cars[4] = {"Tesla", "BMW", "Ford", "Audi"};

    cout << "Here is the list of your cars: \n\n";
    for (int i = 0; i < 4; i++)
    {
        cout << cars[i] << "\n";
    }

    cout << "\n\nAnd Here is the list of your cars along with their index no.: \n\n";
    for (int i = 0; i < 4; i++)
    {
        cout << i << ": " << cars[i] << endl;
    }

    return 0;
}