OOP:


    1. Object: 
    2. Class 
    3. Incapsulation
    4. Inheritance
    5.
    
int(x) = 5 
#isme object kon hai?

>>> x  Object hai.

"Jisko hum variable kahte hai. Python usko Object bolta hai."


    2. class:
    
int(x) = 5    
#is example me class koun hai?
>>> 'int' class hai. yaha par.


True ka class kya hai?
>>>bool hai. 


    #jyada difficult kya hai. class ko banana ya object ko banana.
    
    >>> of course class ko banana kyuki object to variable hai. usko to x = 2. kar diye. aur ban gaya.
    
    >>> class for example str (string) ko banane me jyada mehnat laga hoga. rule sab banane me ki koun koun sa functionality rakhenge. .upper() rakhna .lower() rakhna. 
    >>> list me .append() rakna. slice functionality rakhna etc.
    
    To OOP me yahi karna hota hai. khud ka class banane ke concept ko hi OOP me kiya jata hai.
    Object Oriented programming me yahi hota hai. ek banda apna custom class banata hai. aur saare log object(variable) bana bana kar ke us class (data type) ko use karte hai.
    
    
    
    
    Ab agar Class khud ka banaana hai to usme 2 hi cheej daal sakte hai. 
    
        1. Data or property
        2. Function or behaviour
        
Benefits of OOP:         

    1. Ease of Code
    2. Modularity.(code alag alag module me divide ho gaya. ek jagah class ka logic hai. doosre jagah usko use kar rahe hai. to agar us file me koi error eayega to bhi hamara doosre file safe rahenge kyuki hamara logic wala module safe hai.)
    3. Reusability ( Ek hi class se bahut se function(method) bana sakte hai.)
    4. Readability (For example humko pata karna hai. fraction ka logic kya hai. to fraction wala file class open kiya library se aur sara logic padh liya.)
    5. Efficiency. (Companies ko bas yahi chahiye. aur ye saare benefits ek programmer ya employee ke efficiency ko badhate hai.)
    
    "Objected Oriented Programming is the True way of Programming. at an Application."
    
    
    
    
    
    Lecture 2:
    
    
    Variables in OOP: 
    
    1. Class Variable: Ye Variable ka value poore class me har kisi variable ke liye same hota hai. isko class ke naam se likha jata hai. e.g., Atm.IFSCcode()
    Atm.branch()
    Atm.coutner()
    
    #Definition: Class variables also known as static variables are declared with the static keyword in a class, but outside a method, constructor or a block. There would only be one copy of each class variable per class, regardless of how many objects are created from it.
    
    
    2. Instance Variable: Ye Variable ka value class ke har variabl ke liye alag alag hoga.  isko us variable ke naam se likha jata hai. e.g., 
    'arsh.balance()
    'arsh.AccNo()'
    'arsh.pin()'
    
    
    
    
    'Instance Variable': ek hi variable me alag alag value ek hi time me assing ho. 
                    e.g., atm me balance variable ek hi rahta hai. lekin wo har costomer ke liye alag alag ho jata hai. jaise: 'rohan.balance() = 2000, 
                             'arsh.balance() = 1500,
                             'babu.balance() = 3000.'
                             
          In class-based, object-oriented programming, an instance variable is a variable defined in a class (i.e. a member variable), for which each instantiated object of the class has a separate copy, or instance. An instance variable has similarities with a class variable,[1] but is non-static. 
          
          
          
    3. 'Incapsulation': 
    
    apne code ko "get" aur "set" ka use kar ke Private private banane ka tarika. 
    
    par Python me kuch bhi cheej private nahi hai. kyuki 
        "Python is made for Adults".
        "Jo kaam aap baatcheet se kar sakte ho ki is code ko chedna nahi hai. ye seniors ke liye hai. uske liye ek extra privacy ka layer chadha ke kya hoga."
        "agar Java ke tarah private banaya gaya hota. aur ek senior code ko private kar ke mar gaya." " ab agar us code ko edit karna hai. to kaise hoga."
        
    
     4. "Inheritance":  AApke program me jo bhi cheej repeat ho raha hai. usko parent class bana do. ya grand parent class bana do. agar kisi application me programming karte samay apni efficiency badhana chahte hai. to ye har baar sochna padega ki programming karte samay hum is "inheritance" ko kaise bahut jyada use kar sakte hai. 
     
     
     5. "Polymorphism": 
      agar parent class me aur child class me. dono me koi function hai. aur dono function ka "naam" same hai. to agar usko call karenge to child class ka function ka value return hoga. 
      e.g., baap me ek function "Usool" naam se hai. aur bete me bhi koi function "Usool" naam se hai. to agar us fuction ko use karenge to bete ka "Usool" return hoga. kyuki baap ka usool ab matter nahi karta hai. pariwar ka kya hoga. ghar, gahar jaise hoga ki nahi ye ab bete ke "Usool" par matter karta hai.
      # This is called Method overriding.
      
      
      
      "Method Order Resolution": Agar ek class doosre class se inherit kar raha hai. to kiska function execute hoga conflict create hone me. ye decide hoga Method Order Resolution se. 
     
     
     
    
    

                  
    
    

    
    
    
    
    
    
    




