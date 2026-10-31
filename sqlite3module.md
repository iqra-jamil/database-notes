-  Learn the Python sqlite3 module.
-  Understand connecting to a database.
-  Execute SQL from Python.
-  Learn about committing transactions and closing connections.
-  Understand parameterized queries and why they matter for security.
## Note :":memory:" creates a temporary database that lives only in your computer’s RAM instead of a file on disk. It’s used for quick tests or practice because nothing is saved, and everything disappears when the connection closes or the program ends.
## the transaction, meaning the group of changes made since your last commit.
# 1. How to connect Python to a SQLite database. 
### sqlite3
- if we are using python to create our application and want to use SQLite database we can connect our python application to database using sqlite3 module
- sqlite3 is a built-in module which python include so we dont need to install it
### how to connect both :
- we can call connect() function of sqlite with db file name 
- if file dosent exist SQLite creates it
- the function connect() will return connection object back ,now we can use that object to commit changes ,craete cursor ,close connection etc
# 2. How to execute SQL queries using Python.
- fisrt we connect our application to the db ,it will return a connection object to which we willl ask for cursor
- cursor is a tool which will send our SQL to the database 
- then we will use the execute method of cursor in which we will give our sql as a txt
- like " SELECT * FROM tablename"
- so the order is connect, cursor,execute
# 3. How to insert, retrieve, update, and delete records
-  each operation is jsut a different SQL command we will pass to our execute method of cursor as a txt .
- for each command like INSERT,UPDATE,DELETE the change is only saved only once we commit on connection
# 4. How and why to use `commit()` and `close()`.
#### commit():
- commit saves our chnages to the database
- untill we call commit() on connection, chnages like (update,insert delte) are only temporary and are lost when the program ends.
- we need to call it only after any command that changes data ,but not for SELECT command bcz wo srf data ko read krhi hai
####  close(): 
- ends teh connection to teh database 
- we call it when we're finished so that the file closed and resources are realesed properly
- ANy changes we haven't commited before closing the program will be lost/discarded

#  5. How to retrieve query results using fetchone() and fetchall().
- A query result is the data the database sends back after you run a SELECT: the rows that match your query.
- The cursor sends your SQL to the database, and the matching rows come back to the cursor, where they wait until you read them with fetchone() or fetchall().
#### fetchone():
- it gives us the only one record , the nxt unraed one .
- when we call it again it will give us the nxt row .
- when no row will be left it will return us None



####  fetchall():
- it will give us all the rows of query result, as a list 
- A tuple is a fixed group of values in parentheses, like (1, "Ali", 20). Each row from our query comes back as one tuple, with one value for each column, in the same order as the columns.

#### Note: Use fetchone() when you need just one record, and fetchall() when you want everything.


# 6. parameterized queries and why they matter for security.
#### what are  parameterized queries ?
- A parameterized query (also known as a prepared statement) is a SQL query template that uses placeholders instead of embedding user-input values directly into the query text.
- in MySQL / SQLite	Placeholder Style is Positional (?)
#### why they matter for security.?
It matters because the database treats those values only as data, never as SQL commands. If you instead glue user input into the SQL text, someone could type SQL code as their input and trick the database into running it. That attack is called SQL injection.

Definition: A parameterized query is an SQL statement where the values are replaced by placeholders and passed separately when the statement runs, so the database always treats them as data and never as SQL code. This is what protects you from SQL injection.

Example: In sqlite3, the placeholder is a question mark ?. Instead of typing “iqra”, 90 and the email inside the SQL string, you put one ? for each value. Then you pass the real values as a tuple, as the second argument of execute().
# we can chk executemany () later
if we are adding too many INSErt,or too many UPDATE we can use executemany instead of execute 
- we can make a list of tuples (holding data) and then pass that list + command as an argumnt 
- for all insert diffrent execute will be used 
- for all update commands diffrent execute will be used  and so on