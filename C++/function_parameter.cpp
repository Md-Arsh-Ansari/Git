#include <iostream>
using namespace std;

// The following example has a function that takes a string called fname as parameter. When the function is called, we pass along a first name, which is used inside the function to print a professional name:
void myfunction(string fname)
{
    cout << "Dr. " << fname << endl;
}

// Our tipical main function.
int main()
{
    myfunction("Lily");
    myfunction("Jimmy");
    myfunction("Ben");

    return 0;
}
//When a parameter is passed to the function, it is called an argument. So, from the example above: fname is a parameter, while Lily, Jimmy and Ben are arguments.