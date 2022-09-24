#include <iostream>
using namespace std;

// The following example has a function that takes a string called fname as parameter. When the function is called, we pass along a first name, which is used inside the function to print a professional name:
void myfunction(string fname = "Unknown")
{
    cout << "Dr. " << fname << endl;
}

// Our tipical main function.
int main()
{
    myfunction("Lily");
    myfunction("Jimmy");
    myfunction("Ben");
    myfunction();
    myfunction();

    return 0;
}
// A parameter with a default value, is often known as an "optional parameter". From the example above, fname is an optional parameter and "Unknown" is the default value.