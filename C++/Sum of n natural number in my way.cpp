#include <iostream>
using namespace std;

int main() 
{
  int n;
  
  cout << "Enter the value of n: "<< endl;
  cin >> n;
  
  
  int i = 1;
  int x = 0; 
  
  while( i <= n){
    x = x + i;
    i++;
  }
  
  cout<< "Sum from " << 1 << " to " << n << " = " << x;
  
   
    return 0;
} 