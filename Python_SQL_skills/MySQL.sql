sudo mysql -u root
mysql -u root -p

status

show databases;

create database db1;


'use Db1'
--within the MySQL shell, switch to the database using the USE statement:



show tables;     OR      show tables from Db1;
--    to get a list of all tables:


select * from EMPLOYEE;

select Job from EMPLOYEE;




    CREATE TABLE: 

CREATE TABLE NEWEMPLOYEE ( 
  Emp_NO INTEGER PRIMARY KEY,
  Emp_Name TEXT NOT NULL,
  Emp_Add TEXT NOT NULL,
  Emp_Phone TEXT NOT NULL,
  Dept_No TEXT NOT NULL,
  Dept_Name TEXT NOT NULL,
  Salary TEXT NOT NULL
);


INSERT INTO NEWEMPLOYEE VALUES (0001, 'Ramesh', 'GNoida','9855498465', '3445', 'Sales','25000');
INSERT INTO NEWEMPLOYEE VALUES (0002, 'Suresh', 'GNoida','98565498465', '0072', 'Sales','75000');
INSERT INTO NEWEMPLOYEE VALUES (0003, 'Rajesh', 'GNoida','9855497865', '2324', 'Sales','28000');
INSERT INTO NEWEMPLOYEE VALUES (0004, 'Shyamu', 'BSB','9853698465', '8883', 'Sales','35000');
INSERT INTO NEWEMPLOYEE VALUES (0005, 'Ramu', 'BSB','9855498235', '74568', 'Sales','96000');
INSERT INTO NEWEMPLOYEE VALUES (0006, 'Mahesh', 'GNoida','9851678465', '1238', 'Sales','25000');
INSERT INTO NEWEMPLOYEE VALUES (0007, 'Chaman', 'BSBS','9856723465', '7634', 'D10','215000');



select Emp_Name, Emp_Phone, Dept_Name, Salary from NEWEMPLOYEE;





SELECT DISTINCT Job FROM EMPLOYEE;
--The SELECT DISTINCT statement is used to return only distinct (different) values.

--Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.




SELECT COUNT(DISTINCT Job) FROM EMPLOYEE; 
--The following SQL statement counts and returns the number of different (distinct) countries in the "Customers" table:



SELECT * FROM EMPLOYEE WHERE Job = 'ANALYST';
--It is used to extract only those records that fulfill a specified condition.



'The MySQL AND, OR and NOT Operators'
    SELECT * FROM EMPLOYEE 
    WHERE Job = 'ANALYST' AND Commission = '100';
    
    SELECT * FROM EMPLOYEE 
    WHERE Job = 'MANAGER' OR Job = 'PRESIDENT';
    
    SELECT * FROM EMPLOYEE 
    WHERE Job = 'MANAGER' OR Job = 'PRESIDENT';
    

--Combining AND, OR and NOT    
    SELECT * FROM EMPLOYEE 
    WHERE Job = 'ANALYST' AND (DEPTCODE = '50' OR DEPTCODE = '20');
    
    SELECT * FROM EMPLOYEE 
    WHERE NOT Job = 'MANAGER' AND NOT Job = 'PRESIDENT';



The MySQL ORDER BY Keyword:

    SELECT * FROM EMPLOYEE
    ORDER BY Job;
    --The ORDER BY keyword is used to sort the result-set in ascending or descending order. 
    
    --The ORDER BY keyword sorts the records in ascending order by default. To sort the records in descending order, use the DESC keyword.
    
    
    SELECT * FROM EMPLOYEE ORDER BY Salary DESC;

    

INSERT INTO Example:

    INSERT INTO EMPLOYEE (EmpFName, EmpLName, Job, Salary, DEPTCODE)
    VALUES ('TOM', 'SMITH', 'DATA SCIENTIST', '6000', '50');
    --The INSERT INTO statement is used to insert new records in a table.
    --1. This is the first way: Specify both the column names and the values to be inserted:
    
    INSERT INTO EMPLOYEE
    VALUES ('9865', 'BRAIN', 'TRACY', 'DATA SCIENTIST', '7830', '2015-05-08', '5500', '300', '50');
    -- 2. This is the second way. If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table.
    
    
    
    What is a NULL Value?
    A field with a NULL value is a field with no value.

    If a field in a table is optional, it is possible to insert a new record or update a record without adding a value to this field. Then, the field will be saved with a NULL value.
    Note: A NULL value is different from a zero value or a field that contains spaces. A field with a NULL value is one that has been left blank during record creation!


'The IS NULL Operator'
--The IS NULL operator is used to test for empty values (NULL values).
    
    SELECT * FROM EMPLOYEE WHERE DEPTCODE IS NULL;
    
    SELECT * FROM EMPLOYEE WHERE HireDate IS NULL;

--Tip: Always use IS NULL to look for NULL values.
--Similarly The IS NOT NULL operator is used to test for non-empty values (NOT NULL values).



    
    

UPDATE Table:
The UPDATE statement is used to modify the existing records in a table.

    UPDATE EMPLOYEE 
    SET EmpFName = 'WILL', Manager = '7830', HireDate = '2016-05-09' 
    WHERE SALARY = 6000;
    
UPDATE Multiple Records
It is the WHERE clause that determines how many records will be updated.

    UPDATE EMPLOYEE 
    SET DEPTCODE = '40'
    WHERE Job = 'ANALYST';  
--Be careful when updating records. If you omit the WHERE clause, ALL records will be updated




SQL DELETE: 

--INSERT INTO EMPLOYEE (EmpFName, EmpLName)
--VALUES ('TOMMMMM', 'Smitah')

    DELETE FROM EMPLOYEE WHERE EmpFName = 'TOMMMMM';


'LIMIT Examples'
The following SQL statement selects the first three records:

    SELECT * FROM EMPLOYEE
    LIMIT 3;
    
--'LIMIT with WHERE:
    SELECT * FROM EMPLOYEE WHERE Job = 'ANALYST' LIMIT 2;
    
    

'MIN() and MAX() Functions'
The MIN() function returns the smallest value of the selected column.

The MAX() function returns the largest value of the selected column.

    SELECT MIN(Salary) FROM EMPLOYEE;   
    
    SELECT MIN(Salary) AS MinimumSalary FROM EMPLOYEE;
    --Could also write in this way.
    
    'MAX':
    
    SELECT MAX(Salary) FROM EMPLOYEE; 
    
    SELECT MAX(Salary) AS MaximumSalary FROM EMPLOYEE;
    
  
    
'COUNT(), AVG() and SUM() Functions':
    The COUNT() function returns the number of rows that matches a specified criterion.
    The AVG() function returns the average value of a numeric column. 
    The SUM() function returns the total sum of a numeric column. 
    
    SELECT COUNT(EmpCode) FROM EMPLOYEE;
    
    SELECT AVG(Salary) FROM EMPLOYEE;
    
    SELECT SUM(Salary) FROM EMPLOYEE;



LIKE 'Operator':
--The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

WHERE CustomerName LIKE 'a%'	: Finds any values that start with "a"

WHERE CustomerName LIKE '%a'	: Finds any values that end with "a"

WHERE CustomerName LIKE '%or%'	: Finds any values that have "or" in any position

WHERE CustomerName LIKE '_r%'	: Finds any values that have "r" in the second position

WHERE CustomerName LIKE 'a_%'	: Finds any values that start with "a" and are at least 2 characters in length

WHERE CustomerName LIKE 'a__%'	: Finds any values that start with "a" and are at least 3 characters in length

WHERE ContactName LIKE 'a%o'	: Finds any values that start with "a" and ends with "o"

    
    
    SELECT * FROM EMPLOYEE WHERE EmpFName LIKE 'A%';
        --The following SQL statement selects all customers with a CustomerName starting with "a":
        
    SELECT * FROM EMPLOYEE WHERE EmpLName  LIKE 'mat%';
    --The following SQL statement selects all customers with a City starting with "mat":
    

    SELECT * FROM EMPLOYEE WHERE EmpFName LIKE '%a%';
        --The following SQL statement selects all customers with a CustomerName that have "a" in any position:
     
      
    SELECT * FROM EMPLOYEE WHERE EmpFName  LIKE '%on%';
        --The following SQL statement selects all customers with a City starting with "ber":
        
        
    SELECT * FROM EMPLOYEE WHERE EmpFName NOT LIKE 'a%';
        --The following SQL statement selects all customers with a CustomerName that does NOT start with "a":
        
        
IN Operator:
The IN operator allows you to specify multiple values in a WHERE clause.
The IN operator is a shorthand for multiple OR conditions.

 
    SELECT * FROM EMPLOYEE WHERE Job IN ('DATA SCIENTIST', 'ANALYST', 'MANAGER');
    --SQL statement selects all EMPLOYEE that are 'DATA SCIENTIST', 'ANALYST', 'MANAGER'.
    
    SELECT * FROM EMPLOYEE WHERE Job NOT IN ('DATA SCIENTIST', 'ANALYST', 'MANAGER');
    --SQL statement selects all EMPLOYEE that are "Not"  a 'DATA SCIENTIST', 'ANALYST' or 'MANAGER'.
    
    
    
BETWEEN Operator
The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates.
The BETWEEN operator is inclusive: begin and end values are included.


    SELECT * FROM EMPLOYEE WHERE Salary BETWEEN 4000 AND 7000;
    --As 'Between" operator is inclusive it will also include 7000 and if 4000 is available it will include 4000 also.
    
    
    SELECT * FROM EMPLOYEE WHERE EmpFName BETWEEN 'KEVIN' AND 'SAM' ORDER BY EmpFName;
    -- You could also write it in this way: 
    --SELECT * FROM EMPLOYEE WHERE EmpFName BETWEEN 'KEVIN' AND 'SAM';
    
    


'Aliases':
--Aliases are used to give a table, or a column in a table, a temporary name.

--Aliases are often used to make column names more readable.

--An alias only exists for the duration of that query.

-An alias is created with the AS keyword.


    
    
    SELECT EmpCode AS Id, EmpFName as FirstName  FROM EMPLOYEE;

    SELECT EmpCode AS Id, EmpFName as "First Name"  FROM EMPLOYEE;
    -- Note: Single or double quotation marks are required if the alias name contains spaces:
    
    
    SELECT EmpCode, CONCAT_WS(' ', EmpFName, EmpLName) AS "Full Name"  FROM EMPLOYEE;
    -- It will combine two columns.
    
    
    
UNION Example:



    select DEPTCODE from EMPLOYEE
    UNION 
    SELECT DEPTCODE from DEPARTMENT
    ORDER BY DEPTCODE;
    --statement returns the (only distinct values) of DEPTCODE from both the EMPLOYEE and DEPARTMENT.
    
    
    
    --Note: If some customers or suppliers have the same city, each city will only be listed once, because UNION selects only distinct values. Use UNION ALL to also select duplicate values!
    
    select DEPTCODE from EMPLOYEE
    UNION ALL
    SELECT DEPTCODE from DEPARTMENT
    ORDER BY DEPTCODE;    
    


GROUP BY Examples:   
--The following SQL statement lists the number of Employee code(no. of employee) in each Job Domain.

    SELECT COUNT(EmpCode), Job
    FROM EMPLOYEE
    GROUP BY Job;
    
    
    SELECT COUNT(EmpCode), Job
    FROM EMPLOYEE
    GROUP BY Job;
    ORDER BY COUNT(EmpCode) DESC;
    -- Sorted High to low.
    
    
    
    
HAVING Examples:


    SELECT COUNT(EmpCode), Job
    FROM EMPLOYEE
    GROUP BY Job
    HAVING COUNT(EmpCode) > 2;
    --list all the Job domain where number of Employee is greater than 2
   
   --Note : Here The HAVING clause was added to SQL because the WHERE keyword cannot be used with aggregate functions.
   
   
   
    SELECT COUNT(EmpCode), Job
    FROM EMPLOYEE
    GROUP BY Job
    HAVING COUNT(EmpCode) > 2
    ORDER BY COUNT(EmpCode) DESC;
    --Will list the same but sorted high to low.
    


CASE Statement:

    SELECT EmpFName, Salary,
    CASE WHEN Salary > 3300 THEN 'The Salaray is greater than Average(3300)'
    WHEN Salary = 3300 THEN 'The quantity Average'
    ELSE 'The quantity is Below Average(3300)'
    END AS SalaryTest
    FROM EMPLOYEE;
    
    
    SELECT EmpFName, EmpCode, Salary
    FROM EMPLOYEE
    ORDER BY
    (CASE
        WHEN EmpCode IS NULL THEN Salary
        ELSE EmpCode
    END);
    
  ----------------------------------------------------------------------------------------------------------------  
    
                                'MySQL Database'
                                
                                
DROP DATABASE Db99;
--The DROP DATABASE statement is used to drop(delete) an existing SQL database.
Note: Be careful before dropping a database. Deleting a database will result in loss of complete information stored in the database!

    
    
Create Table Using Another Table:
    
    
    CREATE TABLE Emp 
    AS SELECT Emp_Name, Dept_Name 
    FROM NEWEMPLOYEE;    
    


TRUNCATE TABLE:
--The TRUNCATE TABLE statement is used to delete the data inside a table, but not the table itself.
    
   TRUNCATE TABLE Emp;
   --Now the Table is completely empty.
       

Dropping a Table: 
--Note: Be careful before dropping a table. Deleting a table will result in loss of complete information stored in the table!

    DROP TABLE Emp;
    --Emp table deleted succesfully.
    
    
 
ALTER TABLE Statement
--The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.

--The ALTER TABLE statement is also used to add and drop various constraints on an existing table.   


    --The following SQL adds an "Email" column to the "DEPARTMENT" table:
    ALTER TABLE DEPARTMENT
    ADD Email varchar(255);
    
    
    
    ALTER TABLE DEPARTMENT   
    ADD DateOfBirth date;
    --Notice that the new column, "DateOfBirth", is of type date and is going to hold a date. The data type specifies what type of data the column can hold. 



    --The following SQL deletes the "Email" column from the "DEPARTMENT" table:
    ALTER TABLE DEPARTMENT
    DROP COLUMN Email;
    
      
    #Change Data Type OF COLUMN: 
    
    ALTER TABLE DEPARTMENT  
    MODIFY COLUMN DateOfBirth year;
    --Notice that the "DateOfBirth" column is now of type year and is going to hold a year in a two- or four-digit format.
    
    
    
    
'Constraints': 

/*


Create Constraints
Constraints can be specified when the table is created with the CREATE TABLE statement, or after the table is created with the ALTER TABLE statement.


SQL constraints are used to specify rules for the data in a table.

Constraints are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. If there is any violation between the constraint and the data action, the action is aborted.

Constraints can be column level or table level. Column level constraints apply to a column, and table level constraints apply to the whole table.

The following constraints are commonly used in SQL:

NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Prevents actions that would destroy links between tables
CHECK - Ensures that the values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column if no value is specified
CREATE INDEX - Used to create and retrieve data from the database very quickly
*/


    
1. NOT NULL Constraint:
The NOT NULL constraint enforces a column to NOT accept NULL values.



    --The following SQL ensures that the "ID", "LastName", and "FirstName" columns will NOT accept NULL values when the "Persons" table is created:
    CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Age int
    );
    
   
    'NOT NULL on ALTER TABLE':
    
    ALTER TABLE Persons
    MODIFY Age int NOT NULL;

    

2. UNIQUE Constraint
The UNIQUE constraint ensures that all values in a column are different.


    --UNIQUE Constraint on CREATE TABLE
    --The following SQL creates a UNIQUE constraint on the "ID" column when the "Persons" table is created:

    CREATE TABLE Persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int,
        UNIQUE (ID)
    );
    
 
    --To name a UNIQUE constraint, and to define a UNIQUE constraint on multiple columns, use the following SQL syntax:

    CREATE TABLE Persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int,
        CONSTRAINT UC_Person UNIQUE (ID,LastName)
    );


    --UNIQUE Constraint on ALTER TABLE
    --To create a UNIQUE constraint on the "ID" column when the table is already created, use the following SQL:

    ALTER TABLE Persons
    ADD UNIQUE (ID);
    
    --To name a UNIQUE constraint, and to define a UNIQUE constraint on multiple columns, use the following SQL syntax:

    ALTER TABLE Persons
    ADD CONSTRAINT UC_Person UNIQUE (ID,LastName);


    --DROP a UNIQUE Constraint
    --To drop a UNIQUE constraint, use the following SQL:

    ALTER TABLE Persons
    DROP INDEX UC_Person;
    
    
3. 'PRIMARY KEY Constraint'
--The PRIMARY KEY constraint uniquely identifies each record in a table.
Primary keys must contain UNIQUE values, and cannot contain NULL values.
'A table can have only ONE primary key; and in the table, this primary key can consist of single or multiple columns (fields).'


     PRIMARY KEY on CREATE TABLE
    --The following SQL creates a PRIMARY KEY on the "ID" column when the "Persons" table is created:

    CREATE TABLE Persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int,
        PRIMARY KEY (ID)
    );


    --To allow naming of a PRIMARY KEY constraint, and for defining a PRIMARY KEY constraint on multiple columns, use the following SQL syntax:

    CREATE TABLE Persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int,
        CONSTRAINT PK_Person PRIMARY KEY (ID,LastName)
    );
    --Note: In the example above there is only ONE PRIMARY KEY (PK_Person). However, the VALUE of the primary key is made up of TWO COLUMNS (ID + LastName).
    
    
    
    DROP a PRIMARY KEY Constraint
    --To drop a PRIMARY KEY constraint, use the following SQL:

    ALTER TABLE Persons
    DROP PRIMARY KEY;

    
4. 'FOREIGN KEY Constraint'

/*
The FOREIGN KEY constraint is used to prevent actions that would destroy links between tables.

A FOREIGN KEY is a field (or collection of fields) in one table, that refers to the PRIMARY KEY in another table.

The table with the foreign key is called the child table, and the table with the primary key is called the referenced or parent table.
*/

'Look at the following two tables:'

Persons Table
PersonID    	LastName	FirstName	Age
1	    Hansen	    Ola	        30
2	    Svendson	    Tove	    23
3	    Pettersen	    Kari	        20

Orders Table
OrderID	OrderNumber	PersonID
1	    77895	    3
2	    44678	    3   
3	    22456	    2
4	    24562	    1

'Notice that the "PersonID" column in the "Orders" table points to the "PersonID" column in the "Persons" table.

The "PersonID" column in the "Persons" table is the PRIMARY KEY in the "Persons" table.

The "PersonID" column in the "Orders" table is a FOREIGN KEY in the "Orders" table.

The FOREIGN KEY constraint prevents invalid data from being inserted into the foreign key column, because it has to be one of the values contained in the parent table.'

  



5. CHECK Constraint:
--If you define a CHECK constraint on a column it will allow only certain values for this column.


    'CHECK on CREATE TABLE'
    --The following SQL creates a CHECK constraint on the "Age" column when the "Persons" table is created. The CHECK constraint ensures that the age of a person must be 18, or older:

    CREATE TABLE Persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int CHECK (Age>=18)   
    );

    'Multiple columns': 
    To allow naming of a CHECK constraint, and for defining a CHECK constraint on multiple columns, use the following SQL syntax:

    CREATE TABLE Persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int,
        City varchar(255),
        CONSTRAINT CHK_Person CHECK (Age>=18 AND City='Sandnes')
    );
    
    
    ALTER TABLE Persons
    ADD CHECK (Age>=18);
    
    
    ALTER TABLE Persons
    ADD CONSTRAINT CHK_PersonAge CHECK (Age>=18 AND City='Sandnes');



    --DROP a CHECK Constraint
    --To drop a CHECK constraint, use the following SQL:

    ALTER TABLE Persons
    DROP CHECK CHK_PersonAge;



6. DEFAULT Constraint
--The DEFAULT constraint is used to set a default value for a column.
The default value will be added to all new records, if no other value is specified.


    DEFAULT on CREATE TABLE
    --The following SQL sets a DEFAULT value for the "City" column when the "Persons" table is created:

    CREATE TABLE Persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int,
        City varchar(255) DEFAULT 'Sandnes'
    );
    
    
    'The DEFAULT constraint can also be used to insert system values, by using functions like CURRENT_DATE()':

    CREATE TABLE Orders (
        ID int NOT NULL,
        OrderNumber int NOT NULL,
        OrderDate date DEFAULT CURRENT_DATE()
    );
    
    
    
    ALTER TABLE Persons
    ALTER City SET DEFAULT 'Sandnes';
    
    
    --To Drop
    ALTER TABLE Persons
    ALTER City DROP DEFAULT;
    
    
    
    
CREATE INDEX Statement
The CREATE INDEX statement is used to create indexes in tables.

'Note: Updating a table with indexes takes more time than updating a table without (because the indexes also need an update). So, only create indexes on columns that will be frequently searched against.'

    CREATE INDEX idx_lastname
    ON EMPLOYEE (EmpCode);


    --an index on a combination of columns
    CREATE INDEX idx_pname
    ON Persons (LastName, FirstName);

    --Drop.
    ALTER TABLE table_name
    DROP INDEX index_name;
    
    
    
    
----------------------------------------------------------------------------------------------------------------

                                'MySQL through Python':



import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Arsh880@')
print(mydb.connection_id)




import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Arsh880@')
cur = mydb.cursor()
cur.execute("CREATE DATABASE Db2")



import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Arsh880@',
    database= 'Db2')

cur = mydb.cursor()
t = "CREATE TABLE Book(Book_id integer(4), title varchar(20), price float(5,2))"
cur.execute(t)




import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Arsh880@',
    database= 'Db2')

cur = mydb.cursor()
v = "INSERT INTO Book (Book_id, title, price) VALUES (%s, %s, %s)"
b1 = (1, "Python3", 345)
cur.execute(v, b1)
mydb.commit()





sudo mysql_secure_installation

UPDATE mysql.user SET Password=PASSWORD('Arsh880@') WHERE User='root';

mysql -u root -p







--MySQL Password Setting: 

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password by 'Arsh880@';

import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Arsh880@')
print(mydb.connection_id)




-----------------------------------------------------------------
    Not done: 

Aliases
Join: INNER JOIN, LEFT JOIN,  RIGHT JOIN, CROSS JOIN, SELF JOIN, 
HAVING
Exist 
ANY
ALL
INSERT INTO SELECT
IFNULL() and COALESCE() Functions
FOREIGN KEY CONSTRAIN



