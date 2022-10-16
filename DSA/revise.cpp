#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "enter a number: ";
    cin >> n;

    int row = 1;
    while (row <= n)
    {
        int column = 1;
        while (column <= n)
        {
            cout << column;
            column += 1;
        }
        row += 1;
        cout << "\n";
    }

    return 0;
}