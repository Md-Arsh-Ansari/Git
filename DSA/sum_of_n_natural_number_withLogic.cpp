#include <iostream>
using namespace std;

int main()
{
  int n;

  cout << "Enter the value of n: " << endl;
  cin >> n;

  /* Ek chota baccha gamla le ke baitha hua hai jo numbers
  ko pahchanne to janta hai lekin number ke sequence ko
  nahi janta hai. wo kewal gamle se numbers ko uthata hai aur
  chukke me dalta hai. */

  int i = 1;
  int s = 0;

  while (i <= n) /* Bache ko bataenge ki tumhare haath me jo paisa hoga wo user ke input se kam ho sakta hai uske barabar ho sakta hai. usse bada nahi ho sakta hai. */
  {            
    s = s + i; /* Ye "s" ek chukka hai. jisme pahle se chukke
    me rakha hua jisko s bol rahe hai. aur naya recent
    paisa jo recently dalaya jisko "i" bole. jud jata hai.*/

    i++; /* Ye i++ ek bada bacha hai jo us chote bache ko batata
    hai ki ab ye number us gamle se nikalo aur chukke me
    dal do. */
  }

  cout << "Sum from " << 1 << " to " << n << " = " << s;

  return 0;
}



 /* bache ke paas hum gae aur usko bole ki hum jo bhi number bolenge humko 1 se us number tak paisa jod ke do. tumhare paas is gamle me paisa bhara pada hai.*/
 
 /* Ab bacha doud ke jata hai aur ghar se apna ek dabba le ke aata hai. jisme wo apna khilauna rakhta tha */
 /*initially us dabbe me zero rupiya, gamle me tons of money hai. chote bache ke haath me 1 rupya jisko wo nikal raha hai dabbe me rakhne ke liye. We bring a bada bacha to tell chota bacha ki ab kaun sa rupya nikal kar dabbe me dalna hai. kyuki chota bacha ko sequence nahi pata hai.*/
 
/* Cukka = C = 0 , chota bacha ka haath = i = 1, 
 
  
