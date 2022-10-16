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
    
    
Java Type Casting
"Type casting is when you assign a value of one primitive data type to another type."

#In Java, there are two types of casting:

    Widening Casting (automatically) - converting a smaller type to a larger type size
    byte -> short -> char -> int -> long -> float -> double
    

    Narrowing Casting (manually) - converting a larger type to a smaller size type
    double -> float -> long -> int -> char -> short -> byte
    
    
    
    #Widening casting is done automatically when passing a smaller size type to a larger size type:
    int myInt = 9;
    double myDouble = myInt; // Automatic casting: int to double

    System.out.println(myInt);      // Outputs 9
    System.out.println(myDouble);   // Outputs 9.0
    
    
    
    #Narrowing casting must be done manually by placing the type in parentheses in front of the value:
    double myDouble = 9.78d;
    int myInt = (int) myDouble; // Manual casting: double to int

    System.out.println(myDouble);   // Outputs 9.78
    System.out.println(myInt);      // Outputs 9
    
    

#Java Logical Operators
You can also test for true or false values with logical operators.

Logical operators are used to determine the logic between variables or values:

#Operator	Name	    Description	                            Example	Try it
&& 	    Logical and	Returns true if both statements are true	    x < 5 &&  x < 10	
|| 	    Logical or	Returns true if one of the statements is true	x < 5 || x < 4	
!	    Logical not	Reverse the result, returns false if the result is true	!(x < 5 && x < 10)
    
    
    
# String Concatenation
The + operator can be used between strings to combine them. This is called concatenation:

    String firstName = "John";
    String lastName = "Doe";
    System.out.println(firstName + " " + lastName);
    
    
# Double Quote " " :
    String txt = "We are the so-called \"Vikings\" from the north.";
    
    
    
Java Short Hand if...else (Ternary Operator):

#Syntax
    #variable = (condition) ? expressionTrue :  expressionFalse;

    int time = 20;
    String result;
    result = (time < 18) ? "Good day." : "Good evening.";
    System.out.println(result);  # Good evening.

    

Java Switch Statements
Instead of writing many if..else statements, you can use the switch statement.

#The switch statement selects one of many code blocks to be executed:
#Syntax
    switch(expression) {
      case x:
        // code block
        break;
      case y:
        // code block
        break;
      default:
        // code block
    }
    
This is how it works:
    The switch expression is evaluated once.
    The value of the expression is compared with the values of each case.
    If there is a match, the associated block of code is executed.
    The break and default keywords are optional, and will be described later in this chapter
    The example below uses the weekday number to calculate the weekday name:

#Example
    int day = 4;
    switch (day) {
      case 1:
        System.out.println("Monday");
        break;
      case 2:
        System.out.println("Tuesday");
        break;
      case 3:
        System.out.println("Wednesday");
        break;
      case 4:
        System.out.println("Thursday");
        break;
      case 5:
        System.out.println("Friday");
        break;
      case 6:
        System.out.println("Saturday");
        break;
      case 7:
        System.out.println("Sunday");
        break;
    }
    # Outputs "Thursday" (day 4)


The break Keyword
    When Java reaches a break keyword, it breaks out of the switch block.
    This will stop the execution of more code and case testing inside the block.
    When a match is found, and the job is done, it's time for a break. There is no need for more testing.
    
    
#The default Keyword
The default keyword specifies some code to run if there is no case match:
    
    int day = 4;
    switch (day) {
      case 6:
        System.out.println("Today is Saturday");
        break;
      case 7:
        System.out.println("Today is Sunday");
        break;
      default:
        System.out.println("Looking forward to the Weekend");
    }
    # Outputs "Looking forward to the Weekend"
    
    Note: that if the default statement is used as the last statement in a switch block, it does not need a break.
    
    
The Do/While Loop
    The do/while loop is a variant of the while loop. This loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true.

#Syntax
    do {
      // code block to be executed
    }
    while (condition);
    
The example below uses a do/while loop. The loop will always be executed at least once, even if the condition is false, because the code block is executed before the condition is tested:

#Example
    int i = 0;
    do {
      System.out.println(i);
      i++;
    }
    while (i < 5);
#Output:   
    0
    1
    2
    3
    4
    
    
Java For Loop
When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop:

#Syntax
    for (statement 1; statement 2; statement 3) {
      // code block to be executed
    }
    
    
    Statement 1 is executed (one time) before the execution of the code block.

    Statement 2 defines the condition for executing the code block.

    Statement 3 is executed (every time) after the code block has been executed.


#The example below will print the numbers 0 to 4:

#Example
    for (int i = 0; i < 5; i++) {
      System.out.println(i);
    }

#Example explained
    Statement 1 sets a variable before the loop starts (int i = 0).

    Statement 2 defines the condition for the loop to run (i must be less than 5). If the condition is true, the loop will start over again, if it is false, the loop will end.

    Statement 3 increases a value (i++) each time the code block in the loop has been executed.


For-Each Loop
    There is also a "for-each" loop, which is used exclusively to loop through elements in an array:

#Syntax
    for (type variableName : arrayName) {
      // code block to be executed
    }
    
#The following example outputs all elements in the cars array, using a "for-each" loop:
    Example
    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    for (String i : cars) {
      System.out.println(i);
    }


Java Continue
The continue statement breaks one iteration (in the loop), if a specified condition occurs, and continues with the next iteration in the loop.

This example skips the value of 4:

#Example
    for (int i = 0; i < 10; i++) {
      if (i == 4) {
        continue;
      }
      System.out.println(i);
    }
    
    
Java Arrays
To declare an array, define the variable type with square brackets:

    String[] cars;

#We have now declared a variable that holds an array of strings. To insert values to it, you can place the values in a comma-separated list, inside curly braces:

    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};

#To create an array of integers, you could write:

    int[] myNum = {10, 20, 30, 40};


Access the Elements of an Array
#You can access an array element by referring to the index number.

    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    System.out.println(cars[0]);
    # Outputs Volvo

Change an Array Element
#To change the value of a specific element, refer to the index number:

    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    cars[0] = "Opel";
    System.out.println(cars[0]);
    # Now outputs Opel instead of Volvo

Array Length
#To find out how many elements an array has, use the length property:

    Example
    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    System.out.println(cars.length);
    #Outputs 4
    
    
    
Loop Through an Array
You can loop through the array elements with the for loop, and use the length property to specify how many times the loop should run.

#The following example outputs all elements in the cars array:


    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    for (int i = 0; i < cars.length; i++) {
      System.out.println(cars[i]);
    }
        #Volvo
        #BMW
        #Ford
        #Mazda   
        
        
Loop Through an Array with For-Each
There is also a "for-each" loop, which is used exclusively to loop through elements in arrays:

#Syntax
    for (type variable : arrayname) {
      ...
    }
    
The following example outputs all elements in the cars array, using a "for-each" loop:

    #Example
    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    for (String i : cars) {
      System.out.println(i);
    }
    
        #Volvo
        #BMW
        #Ford
        #Mazda
        
The example above can be read like this: 
#for each String element (called i - as in index) in cars, print out the value of i.

If you compare the for loop and for-each loop, you will see that the for-each method is easier to write, it does not require a counter (using the length property), and it is more readable.

    
Multidimensional Arrays
A multidimensional array is an array of arrays.

#To create a two-dimensional array, add each array within its own set of curly braces:

#Example
    int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
    
#myNumbers is now an array with two arrays as its elements.

To access the elements of the myNumbers array, specify two indexes: one for the array, and one for the element inside that array. This example accesses the third element (2) in the second array (1) of myNumbers:

#Example
    int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
    int x = myNumbers[1][2];
    System.out.println(x); // Outputs 7


#We can also use a for loop inside another for loop to get the elements of a two-dimensional array (we still have to point to the two indexes):
    for (int i = 0; i < myNumbers.length; ++i) {
      for(int j = 0; j < myNumbers[i].length; ++j) {
        System.out.println(myNumbers[i][j]);
        
        1
        2
        3
        4
        5
        6
        7
        






