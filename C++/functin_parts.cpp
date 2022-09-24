#include <iostream>
using namespace std;

//Function Declaration
void newfunction();


//Our tipical main function.
int main()
{
    newfunction();
    newfunction();
    newfunction();

    return 0;
}

//Function Definition
void newfunction() {
    cout << "This is a function call\n";
}