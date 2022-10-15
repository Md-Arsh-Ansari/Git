#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Please enter a number: ";
    cin >> n;

    int row = 1;
    while (row <= n)
    {
        int column = 1;
        while (column <= n)
        {
            cout << "*";
            column++;
        }
        cout << "\n";
        row++;
    }

    return 0;
}