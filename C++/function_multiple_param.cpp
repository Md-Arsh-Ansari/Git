#include <iostream>
using namespace std;

// The following example has a function that takes a string called fname as parameter. When the function is called, we pass along a first name, which is used inside the function to print a professional name:
void myfunction(string fname, int age)
{
    cout << "Dr. " << fname << ", " << age << " Years old." << endl;
}

// Our tipical main function.
int main()
{
    myfunction("Lily", 35);
    myfunction("Jimmy", 40);
    myfunction("Ben", 38);

    return 0;
}
// Note that when you are working with multiple parameters, the function call must have the same number of arguments as there are parameters, and the arguments must be passed in the same order.