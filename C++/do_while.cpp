#include <iostream>
using namespace std;

int main() 
{

    
    char input;
    
    do {
      cout << "Hello, This is a program." << endl;
      cout << "it will execute again again." << endl;
      cout << "unless you press: 'x'"<< endl;
      cin >> input;
    }
    while( input != 'x');
   
    return 0;
}