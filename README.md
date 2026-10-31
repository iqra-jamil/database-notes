# Day 1

## SQL basics and tables
Understand how databases organize information.
-  Understand what a database, table, row, and column are.
-  Learn the difference between SQL and a database such as SQLite.
-  Understand data types such as INTEGER, TEXT, REAL, and NULL.
-  Create a database and a table.
-  Insert a few sample users into the table.
-  Practise viewing all records with SELECT.

# What is database??
- database is an organized collection of electronic information,store and acessed 
  from computer 
- A software which acts as a brain of databse used to manage database
- manage (craete,read,update,delte data in the database) 
- Most databases use two ways to store data :
       - tables(like spread sheets with rows and coulumns)
       - flexible documnts(short notes with different fields)
## DBMS :
A database has the DBMS acting like a careful librarian: it decides how data is written, finds things quickly, stops two people from overwriting each other’s changes, and protects the data if something goes wrong.

### Note : a database is organized data stored in files, managed by software that makes it fast, safe, and easy to use without needing to know where it is physically saved.

# databases in LLM applications
- LLM applications usually use two kinds of databases
     - regular databases(tables) to store things like users,chat history
     - vector databases  store txt as lists of numbers(vectors) so that app can find information by meanings/similarity(similar meaning),instead of exact words
- The second kind is what makes RAG wrk


# table,Rows,Columns

### Tables:(relation)
- A table is collection of realted data organized in rows and columns
- A single table can store information about only one type of entity
- for example in a database a table can have an information about student, a product
- we also could have a table called messages that must contain chat messages
- there could be a table containing information about users using our app

### columns:(attributes or fields)
- a coulumn is a vertical field in a table that hold specific attributes of an entity
- every attribute in a coulmn should have same datatype
- for example name column should have names only
- Columns are the headings of the table
### Rows(tuples,columns)
- a row is a single horizontal entry in a table
- that holds one complete record/data of a single instance of entity

# relational database management system
A relational database management system (RDBMS) is a DBMS that stores data in related tables (rows and columns) and uses SQL to manage it, such as MySQL, PostgreSQL, and SQLite.

# difference between SQL and a database such as SQLite
### SQL :
- an SQL (structured query language) used to communicate to the databases
- we write SQL commands to create tables,insert data,update data,search data,delte data from the databse
### SQLite
- SQLitie is a DBMS,a software that manage database
- it store whole database in a single file on our computer's disk
- SQLite understand SQL commands
- its serverless,it dont required a server like traditional DBMS

### NOTE: SQL is only the language you write in, but SQLite is the software that decides which data types exist and how to store them. So you type the data type in SQL, but the list of types belongs to SQLite (the DBMS).

# data types such as INTEGER, TEXT, REAL, and NULL,BLOB.(storage classes)
These are the basic data types in SQLite. A data type defines what kind of value a column can hold.
- INTEGER: Whole numbers, with no decimal point. Example: an age like 21 or an ID like 5.

- TEXT: Characters and words, written inside quotes. Example: a name like “Ali” or an email address.

- REAL: Numbers with a decimal point (floating-point numbers). Example: a price like 19.99 or a height like 5.6.

- NULL: Means “no value” or “unknown”. It is not the same as zero or an empty text. If a student hasn’t given a phone number yet, that cell is NULL.

- BLOB, which stores raw binary data exactly as it is, like an image or a file.

#  Create a database and a table.
## Create a database
- to create a database frst install sqlite3
- sqlite3 is the command-line program that lets you type SQL commands and creates and opens SQLite database files, so it’s the tool we’ll use to practise.
- after installation did somesetup
- after that write sqlite3 filename.db in the command prompt
- we can use .databases to chk the the name and location of the file we just craeted
- we can use .quit to leave
- we can reopen it by typing sqlite3 filename.db
- this command will craete a new folder only when its alredy not created

### SQLite keeps waiting until it sees the semicolon.
## create a table inside database
- to craete a table use this command:
CRETEA TABLE tablename(col1name datatype PRIMARY KEY,col2name datatype,col3name datatype)
- to delete a table use :
 DROP TABLE tablename;
- to see tables names use (to ensure if the table is created or not):
   .tables
- to see how the table was defined use(its columns, their data types, and constraints like PRIMARY KEY.) :
.schema users
- to insert a row we can user 
INSERT INTO tablename (col1name,col2name,col3name) VALUES(col1value,col2value,col3value);
- to view all records from a table use :
 SELECT * FROM tablename;




# Day 2


## CRUD and filtering
Learn to work with stored data.
-  Create records with INSERT.
-  Read records with SELECT.
-  Update records with UPDATE.
-  Delete records with DELETE.
-  Filter records using WHERE.
-  Practise comparison operators, AND, OR, and ORDER BY.
-  Understand why you should use a WHERE condition carefully when updating or deleting records.
  
  Deliverable: Add, search, update, and delete users using SQL.

# Create records with INSERT.
already done
# Read records with SELECT.
already done
#  Update records with UPDATE.
to update a value of a record :(update a record)
UPDATE tablename SET colname = 'updatedvalue' WHERE condition (like  value of the row we want to update)(WHERE ID='4')
#  Delete records with DELETE.
We can use following command to delete a row
DELETE FROM tablename 
WHERE condition

# why we should use a WHERE condition carefully when updating or deleting records.
we should use WHERE clause while updating or deleting a row else it will update or delete all the records

# Practise comparison operators, AND, OR, and ORDER BY  
**Comparison operators**
- **Definition:** Symbols used in a WHERE condition to compare a column's value with another value.
- **List:** `=` equal, `!=` or `<>` not equal, `>` greater, `<` less, `>=` greater or equal, `<=` less or equal.
- **Example:** `ID>2` returns users with ID 3 and above.
- **Remember:** Text values go in single quotes.

**AND**
- **Definition:** Joins two conditions, and a row is returned only if both are true.
- **Example:** `ID=4 AND user_name='iqra4'` returns one row. With `'iqra7'` it returns nothing, because the second part is false.

**OR**
- **Definition:** Joins two conditions, and a row is returned if at least one is true.
- **Example:** `ID=4 OR user_name='iqra7'` returns user 4, because the first part is true.
- **AND vs OR:** AND narrows the result, OR widens it.

**ORDER BY**
- **Definition:** Sorts the returned rows by one or more columns.
- **Options:** `ASC` is smallest to largest or A to Z (the default). `DESC` is largest to smallest or Z to A.
- **Position:** It comes after WHERE and before the semicolon.
- **Example:** Sorting by ID with DESC shows 4, 3, 2, 1.
- **Remember:** It changes the order of the rows, not which rows appear.

# Filter records using WHERE.
- WHERE is a clause that filters rows, so a command returns or affects only the rows that match a given condition.
- It goes after FROM table_name, and you can combine conditions using comparison operators, AND, and OR.


# Day 3


Primary keys and foreign keys
Understand how tables connect.
-  Learn what a primary key does.
-  Understand why each user needs a unique ID.
-  Learn what a foreign key does.
-  Understand one-to-many relationships.
-  Create users and conversations tables.
-  Connect each conversation to its user.
-  Learn what happens when a referenced record does not exist.
  
  Deliverable: Store multiple conversations for one user and connect them correctly.

# what a primary key does.
- Pimary key is a column who values should be unique ,so that each column can be identiffied uniquly
- and cant be reapeted if we do sqlite will give UNIQUE constarint error
- Example: in a messages table, the message ID is the primary key, so each chat message can be found, updated, or deleted without touching any other.
#  why each user needs a unique ID.
- a unique id lets detabase to tell users apart,even if two or more users have same name or same emails etc 
- unique ID make sure if we apply CRUD operations we affect exactly the correct record.
- it is also what other tables use to link to a user,like a messages table storing each message’s user ID to show who sent it.

# what a foreign key does.

- if we define a coulmn as a primary key in 1 table and then use that primary key in another table to link both tables then that primary key will be forign key in other table which we got from one table into another table 
- A foreign key is a column in one table that holds the primary key value of a row in another table, which creates a link between the two tables.
- It makes the database check that the link is valid, so we can’t point to a user who doesn’t exist.


- Example: users and messages

    - users table: user_ID is the primary key (unique for each user).
    - messages table: user_ID is the foreign key, a copy of a value from users.user_ID.
    - Example: message 101 has user_ID = 1, so it belongs to the user with ID 1 (iqra).
    - Benefits: the name is stored only once, and the database rejects a message with a    user_ID that doesn’t exist in users.
    - Same column name in both tables, different roles: primary key in users, foreign key in messages.


# one-to-many relationships
- Definition: A one-to-many relationship is when one row in a table can be linked to many rows in another table, but each of those rows links back to only one.
- Example: One user can send many messages, but each message belongs to only one user.
- How it’s built: The “many” side (messages) holds a foreign key (user_ID) that points to the primary key of the “one” side (users). This is the most common type of relationship in databases.
# Practical: 
## Create users and conversations tables.
craete normal table with a primary key
## Connect each conversation to its user.
craete normal table with a primary key and then use previous table's priamry key as a forieng key here when we are using taht key as a foregn key we need to give define that key name again with datatype while craeting table aslo we tell the reference table name with forign key name 
## Learn what happens when a referenced record of a foreign key does not exist.
- A refrence record is a row to which foreign key points to.
- for example in our case forign key is user_id which is pointing to the rows in table name users
- the task is to chk what db does when we add a row for which foriegn key doesnt exist
   which is called a foreign key violation.
- Example: our users table has IDs 1 to 4. If we insert a message with user_id 99, there is no user 99, so the message points to nobody (an “orphan” record). With foreign key checking on, the database rejects the insert and shows an error. This is how the database protects the link between the tables.
# foreign key constarints
- SQLite has foreign key checking turned off by default
- so frst we turn it on with the following command :
  PRAGMA foreign_keys=ON or 1;
- we need to do this each time we open the database.
- the error will be FOREIGN KEY constraint failed
