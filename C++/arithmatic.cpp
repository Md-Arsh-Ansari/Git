#include <iostream>
using namespace std;

int main() 
{
  int a, b, add, sub, mul, div, mdiv;
  cout<<"Please enter 'a' and 'b': \n";
  cin>>a>>b;
  
  
  add = a + b;
  cout<<"Addition: "<<add<<endl;
  
  sub = a - b;
  cout<<"Subtraction: "<<sub<<endl;
  
  mul = a * b;
  cout<<"Multiplication: "<<mul<<endl;
  
  div = a / b;
  cout<<"Division: "<<div<<endl;
  
  mdiv = a % b;
  cout<<"Modulous: "<<mdiv<<endl;
  return 0;
}