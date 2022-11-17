#include <iostream>
using namespace std;

int main()
{
    int num, dabba = 0, inhand = 1;
    cout << "Please enter a number: ";
    cin >> num;

    while (inhand <= num)
    {
        dabba = dabba + inhand;
        inhand += 1;
    }

    cout << "The sum from 1 to " << num << " = " << dabba << endl;

    return 0;
}