# Day 4

## JOIN
Retrieve related information from multiple tables.
- Learn INNER JOIN.
- Learn LEFT JOIN at a basic level.
- Query conversations belonging to a specific user.
- Retrieve related records from users and conversations.
  
  Deliverable: Write a query that displays a user's name alongside their conversations.

# What is join ??
### Definition :
- An operation can apply on two or more tables to combine their rows into one result
- based on realted or common row (usually the primary key that match with foreign key)

### Example:
- For example we have one table name customer_table with columns:customer_id,customer_name
- we have another table name order_table with columns : order_id ,customer_id
  - we can join both of them based on cusomer_id to find which cutomer with which cutomer name placed which order
- The result is a new temporary table made only for that query. 
- Each row in it is built by combining data from the matching rows of the two tables, and the original tables stay unchanged.


# main types of join:
1. inner join
2. left join (left outer join)
3. right join(right outer join)
4. full join (full outer join)
5. cross join
6. self join


# inner join: 
### Definetion:
- inner join is an operation we apply on two tables to combine thier rows but it return only the records/rows whre the join operation find a match in both tables (common coulumn's value in both table)
- it will skip the records whose common coulumn's value not found in both tables
### Example:
### table_name = Customers
c_id	       name
1	          Ali
2	          Sara
3	          Hina

### table_name = orders
order_id  c_id
order_id	customer_id
101	           1
102	           1
103	           2

### resulted_table
- Joining Customers and Orders where Customers.c_id = Orders.customer_id gives:
name        order_id
Ali            101
Ali            102
Sara          103

- it will skip hina 
- Hina is missing from the result because she has no matching order. Ali appears twice because he has two matching orders.
# left join (left outer join)
- left join operation will return all the rows from left table (taht fullfill the left join condition) + matching rows from right table 
- if a left table's row has no match in the right table it will still return that row but value will be filled with null in right table’s column in result table(it fills the right-table columns (like order_id) because there was nothing to match.)
### Example: Using the same tables, with Customers as the left table. 
name	      order_id
Ali	           101
Ali	           102
Sara	         103
Hina	         NULL

- Hina now appears, even though she has no orders, with NULL in order_id. This is the difference from INNER JOIN, which dropped her.

# Day 5

SQLite and Python
Connect a database to your application.
-  Understand what SQLite is and why it suits small applications and prototypes.
-  Learn how a SQLite database file persists on disk.
-  Learn the Python sqlite3 module.
-  Understand connecting to a database.
-  Execute SQL from Python.
-  Learn about committing transactions and closing connections.
-  Understand parameterized queries and why they matter for security.
  
  Deliverable: Use Python to insert a user and retrieve that user's information from SQLite.

# what SQLite is and why it suits small applications and prototypes.
##  What SQLite is :
- SQLite is an RDBMS (Relational Database Management System)
- SQLite is a lightweight, serverless, self-contained relational database management system
- It stores an entire database in a single file
- is accessed directly through a library inside your application, using SQL,instead of connecting to a separate database server.
### In simple words:
- Most databases (like PostgreSQL or MySQL) run as a separate program called a server.
- our application ahs to connect with that server,like making a phone call.
- SQLite has no server.
- The database is just one file on our disk (for example, app.db), and our app reads and writes that file directly.


## Why it suits small apps and prototypes
1. No setup. You don’t install or configure anything. Python already includes SQLite, so you can start right away.
2. One file. Your whole database is a single file. You can copy it, back it up, email it, or delete it to start fresh.
3. No server to manage. There are no usernames, passwords, ports, or background services to worry about.
4. Free and open source. No cost, no license worries.
5. Fast for small workloads. Because there is no network call, reads are very quick.
6. Still real SQL. It supports tables, relationships, queries, and transactions, so what you learn applies to bigger databases too.
7. Easy to move later. Since it uses standard SQL, you can switch to PostgreSQL when your app grows, without rewriting everything.
## Where it is not a good fit:
- Many users writing at the same time (SQLite allows only one writer at a time).
- Very large data or heavy traffic.
- Apps spread across many servers, since the file lives on one machine.
## Example:
 A personal chatbot, a student project, or a mobile app with local data works great with SQLite. A busy online store with thousands of orders per minute needs something like PostgreSQL.

# how a SQLite database file persists on disk.
## Formal definition:
- Persistence means data is saved on permanent storage (disk), so it stays even after the program closes or the computer restarts.
- SQLite persists by writing all your data into a single file (like app.db) on disk.
## In simple words:
- When you run INSERT or UPDATE, SQLite doesn’t keep the data only in memory (RAM).
- It writes the changes into the app.db file.
- When your app stops and starts again, SQLite opens the same file and your data is still there.
## Example: 
You save 10 chats in your chatbot, close the app, and open it tomorrow. The 10 chats are still there because they were written to app.db.
## How it stays safe:
- SQLite writes changes in transactions.
- A transaction is a group of database operations treated as one unit. It follows “all or nothing”: if every step succeeds, the changes are saved (committed); if anything fails midway, all changes are undone (rolled back).
- Example: You save a chat with 2 steps: (1) save the user’s message, (2) save the bot’s reply. If the power cuts after step 1, SQLite undoes step 1 when it restarts. You won’t end up with a message that has no reply, and your file stays clean.
- A change is either fully saved or not saved at all, so a sudden crash or power cut won’t leave your file half-broken. (will be empty)
## Catch:
On some free hosting platforms, the disk is temporary and gets wiped on restart, so the file may disappear.