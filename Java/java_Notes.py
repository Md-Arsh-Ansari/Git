Every line of code that runs in Java must be inside a class. In our example, we named the class Main. 
A class should always start with an "uppercase first letter".

You should also note that each code statement must end with a "semicolon (;)".




# The Print() Method
There is also a print() method, which is similar to println().

The only difference is that it does not insert a new line at the end of the output:


#Comments: 
Single-line comments start with two forward slashes (//).

Multi-line comments start with /* and ends with */.
Any text between /* and */ will be ignored by Java.


#Declaring (Creating) Variables
To create a variable, you must specify the type and assign it a value:

    type variableName = value;
    
    int myNum = 5;
    float myFloatNum = 5.99f;
    char myLetter = 'D';
    boolean myBool = true;
    String myText = "Hello";

    
    String name = "John";
    System.out.println(name);
    
    
    #First declare then assign it later
    int myNum;
    myNum = 15;
    System.out.println(myNum);
    
    #Declare and assign more than one variable in a bunch.
    int x = 5, y = 6, z = 50;
    System.out.println(x + y + z);
    
    #Assigning the same value to multiple variables in one line:
    int x, y, z;
    x = y = z = 50;
    System.out.println(x + y + z);

#Change the value of myNum from 15 to 20:
    int myNum = 15;
    myNum = 20;  // myNum is now 20
    System.out.println(myNum);
    
    
#Final Variables
"If you don't want others (or yourself) to overwrite existing values, use the final keyword (this will declare the variable as "final" or "constant", which means unchangeable and read-only):"

    final int myNum = 15;
    myNum = 20;  // will generate an error: cannot assign a value to a final variable
    

#The general rules for naming variables are:
    Names can contain letters, digits, underscores, and dollar signs
    Names must begin with a letter
    Names should start with a lowercase letter and it cannot contain whitespace
    Names can also begin with $ and _ (but we will not use it in this tutorial)
    Names are case sensitive ("myVar" and "myvar" are different variables)
    Reserved words (like Java keywords, such as int or boolean) cannot be used as names
    

#Println()
To combine both text and a variable, use the + character:

    String name = "John";
    System.out.println("Hello " + name);
    
    
"Java Data Types":

#Data types are divided into two groups:
    Primitive data types - includes byte, short, int, long, float, double, boolean and char
    Non-primitive data types - such as String, Arrays and Classes (you will learn more about these in a later chapter)   
    
    
#Data    Type    	    Size	Description
byte	    1 byte  	    Stores whole numbers from -128 to 127
short   	2 bytes	    Stores whole numbers from -32,768 to 32,767
int	    4 bytes	    Stores whole numbers from -2,147,483,648 to 2,147,483,647
long	    8 bytes	    Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
float	    4 bytes	    Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits
double  	8 bytes	    Stores fractional numbers. Sufficient for storing 15 decimal digits
boolean 	1 bit	    Stores true or false values
char	    2 bytes	    Stores a single character/letter or ASCII values

 
 
 #What is the importance of above table:
 
 Byte
The byte data type can store whole numbers from -128 to 127. This can be used instead of int or other integer types to save memory when you are certain that the value will be within -128 and 127:


#Use float or double?
The precision of a floating point value indicates how many digits the value can have after the decimal point. The precision of float is only six or seven decimal digits, while double variables have a precision of about 15 digits. Therefore it is safer to use double for most calculations.


 Characters
The char data type is used to store a single character. The character must be surrounded by single quotes, like 'A' or 'c':
    
    
 #The String type is so much used and integrated in Java, that some call it "the special ninth type".
#A String in Java is actually a non-primitive data type, because it refers to an object. The String object has methods that are used to perform certain operations on strings.


  Non-Primitive Data Types
#Non-primitive data types are called reference types because they refer to objects.

#The main difference between primitive and non-primitive data types are:
    Primitive types are predefined (already defined) in Java. Non-primitive types are created by the programmer and is not defined by Java (except for String).
    Non-primitive types can be used to call methods to perform certain operations, while primitive types cannot.
    A primitive type has always a value, while non-primitive types can be "null".
    A primitive type starts with a lowercase letter, while non-primitive types starts with an "uppercase letter".
    The size of a primitive type depends on the data type, while non-primitive types have all the "same size".
    Examples of non-primitive types are "Strings, Arrays, Classes, Interface". etc.
    
    
s    
    

 
    
    
    
    
    
    
    
    
    
    
    








