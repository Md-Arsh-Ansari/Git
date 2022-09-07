#include <iostream>
#include <cmath>
using namespace std;

int main() 
{

    
    int time = 18;
    
    /*
    
    if (time < 10) {
      cout << "Good day.";
    } 
    
    else {
      cout << "Good evening.";
    }
    */
    
    string result = (time < 10) ? "Good Day" : "Good evening.";
    cout << result;
   
    return 0;
}