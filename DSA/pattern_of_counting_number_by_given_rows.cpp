#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Please enter n: ";
    cin >> n;

    int i = 1;
    int x = 1;
    while (i <= n) // it is basically n times.
    {
        int j = 1;
        while (j <= n)
        {
            cout << x << " ";

            j++;
            x++;
        }

        cout << endl; // After printing one row we need to enter the next row. so, endl.
        i++;
    }
    return 0;
}