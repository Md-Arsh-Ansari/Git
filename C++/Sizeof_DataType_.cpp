#include <iostream>
using namespace std;

int main() 
{
    int a = 20;
    float b = 5.2323123;
    char c = 'c';
    double d = 5.2323123;
    
    
    cout<< "Size of Integer= "<< sizeof(a) << " bytes" <<endl;
    cout<< "Size of float  = "<< sizeof(b) << " bytes\n";
    cout<< "Size of double = "<< sizeof(d) << " bytes\n";
    cout<< "Size of char   = "<< sizeof(c) << " bytes\n";
    
   
    return 0;
} 
