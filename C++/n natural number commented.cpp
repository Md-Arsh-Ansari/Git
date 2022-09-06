#include <iostream>
using namespace std;

int main() 
{
  int n;
  
  cout << "Enter the value of n: "<< endl;
  cin >> n;
  
  /* Ek chota baccha gamla le ke baitha hua hai jo numbers
  ko pahchanne to janta hai lekin number ke sequence ko 
  nahi janta hai. wo kewal gamle se numbers ko uthata hai aur 
  chukke me dalta hai. */
  
  int i = 1;
  int s = 0; 
  
  while( i <= n){ /* Ye iterate karne ke liye hai */
    s = s + i; /* Ye "s" ek chukka hai. jisme pahle se chukke
    me rakha hua jisko s bol rahe hai. aur naya recent
    paisa jo recently dalaya jisko "i" bole. jud jata hai.*/
    
    i++; /* Ye i++ ek bada bacha hai jo us chote bache ko batata
    hai ki ab ye number us gamle se nikalo aur chukke me
    dal do. */
    
  }
  
  cout<< "Sum from " << 1 << " to " << n << " = " << s;
  
   
    return 0;
} 