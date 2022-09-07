#include <iostream>
using namespace std;

int main() 
{

    
  char button;
  cout<< "Please type a button: ";
  cin >> button;
  
  
  switch (button) 
  {
    case 'a':
      cout << "Assalamu Alaikum";
      break;
    
    case 'b':
      cout << "Hola";
      break;
    
    case 'c':
      cout << "Hi";
      break;
    
    case 'd':
      cout << "Hello";
      break;
       
    case 'e':
      cout << "Good Morning";
      break;
       
    default:
      cout << "I am still learning!";   
       
  }
    
   
    return 0;
}