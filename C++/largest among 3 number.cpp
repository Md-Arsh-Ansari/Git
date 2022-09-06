#include <iostream>
using namespace std;

int main() 
{
    int a = 2;
    int b = 5;
    int c = 88;
    
    
    /* Logic = 3 number hai 3 no number hai. pahla no. ko
    doosre se compare karenge. pass ho jata hai. to us pahle
    phir se teesre number see compare karenge. 
    
    Agar pahle no. ko doosre no se compare kare aur fail
    ho jae to phir doosre no. ko teesre se compare karenge.
    */
    
    if ( a > b ) {
      if ( a > c ) { /* Is program me yahi dikkat hai yaha
      par nested loop lag raha hai. kyuki a naam ke variable
      se hi compare karna padega.  */
        cout << "a = " << a << " is max";
      }
      else {
        cout << "c = " << c << " is max";
      }
    }
    
    
    else if ( b > c ){
        cout << "b = " << b << " is max";
      }
      else {
        cout << "c = " << c << " is max";
      }
    return 0;
}