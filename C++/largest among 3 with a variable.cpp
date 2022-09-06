#include <iostream>
using namespace std;

int main() 
{
    int a = 2;
    int b = 1;
    int c = 0;
    int m = 0;
    
    
    /* Hamare paas 3 dabba hai jiska naam a, b, aur c hai.
    hum nested loop se bachne ke liye. ek aur dabba le
    aaenge. jiska naam hoga "m". jisme 0 dala hua hai.
    
    Ab a ko sabse pahle m se compare karenge. jisme 0 dala
    hua hai. to a dabbe ke value ko utha kar hum m dabbe me 
    daal denge.
    
    ab a dabbe ka koi kaam nahi hai. ab b ko compare karenge 
    m se jisme ki a dabbe ka value present hai.
    agar b bada ho jata hai m se. to m dabbe me a ke value 
    ko hata ke b ke value ko bhar denge.
    agar b chota hai m se to m dabbe me a ka hi value present
    rahega. 
    
    ab m ko lastly c se compare karenge. agar c bada ho jata 
    hai m ke. to m me present value ko c ke value se replace 
    kar denge.
    
    aur lastly m ko print kar denge.
    
    */
    
    if ( a > m ) {
      m = a;
    }
    
    if ( b > m) {
      m = b;
    }
    
    if ( c > m ) {
      m = c;
    }
    
    cout << "Largest number = " << m;
    return 0;
}